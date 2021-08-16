from datetime import datetime
from time import sleep
from gpiozero import RGBLED

from src.main.config import SystemConfig
from src.main.controllers.lighting.lighting_config import LightingConfig
from src.main.controllers.lighting.natural_colors import NaturalColors
from src.main.utils.color_functions import ColorFunctions
from src.main.utils.colors import Colors
from src.main.utils.rgb_color import RgbColor
from src.main.utils.time_functions import TimeFunctions

lightingConfig: LightingConfig = SystemConfig.lighting

TEST = NaturalColors.LATE_EVENING

class LightingController:
	
	def __init__(self):
		self.led = RGBLED(lightingConfig.GPIO.R, lightingConfig.GPIO.G, lightingConfig.GPIO.B, False)
		self.led.off()
		self.start_time = lightingConfig.START_TIME
		self.duration = lightingConfig.DURATION
		self.min_brightness = lightingConfig.MIN_BRIGHTNESS
		self.max_brightness = lightingConfig.MAX_BRIGHTNESS
		self.color_steps = []
		self.enabled = False

	def start(self):
		self.enabled = True
		self.realtime()

	def stop(self):
		self.enabled = False
		self.led.off()

	def generateColorSteps(self):
		self.color_setps = ColorFunctions.interpolate_rgb_gradient(lightingConfig.COLORS, self.start_time*60)

	def getColorForTime(self, time: datetime) -> RgbColor:
		if TimeFunctions.within_range(time, self.start_time, self.start_time + self.duration):
			minute_of_day = TimeFunctions.minute_of_day(time)
			offset = self.start_time * 60
			return self.color_steps[minute_of_day - offset]
		else:
			return Colors.BLACK

	def getBrightnessForTime(self, time: datetime) -> float:
		return TimeFunctions.cosine_interpolation(time, self.start_time, self.duration, self.min_brightness, self.max_brightness)

	def demo_single(self):
		self.led.color = TEST.as_percents()
		while True:
			sleep(1)

	def demo_colors(self):
		colors = [NaturalColors.EVENING, NaturalColors.LATE_EVENING, NaturalColors.DUSK, NaturalColors.NIGHT]
		counter = 0
		while True:
			color = colors[counter%len(colors)]
			color_percent = color.as_percents()
			print(color.as_rgb(), color_percent)
			self.led.color = color_percent
			counter+=1
			sleep(1)

	def demo(self):
		self.generateColorSteps()
		for h in range(self.start_time, self.start_time + self.duration):
			for m in range(0, 60):
				now = datetime(2021, 8, 8, h, m, 0)
				self.updateLED(now)
				sleep(0.1)

	def realtime(self):
		self.generateColorSteps()
		while self.enabled:
			now = datetime.now()
			self.updateLED(now)
			sleep(60)

	def updateLED(self, now):
		brightness = self.getBrightnessForTime(now)
		color = self.getColorForTime(now).brightness(brightness)
		print(now, brightness, color.as_percents())
		self.led.color = color.as_percents()
