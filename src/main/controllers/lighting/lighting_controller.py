from datetime import datetime
from importlib import util as importlib_util
import threading

from src.main.controllers.controller import Controller
from src.main.controllers.lighting.lighting_config import LightingConfig
from src.main.controllers.lighting.natural_colors import NaturalColors
from src.main.utils.clamp import clamp
from src.main.utils.color_functions import ColorFunctions
from src.main.utils.colors import Colors
from src.main.utils.rgb_color import RgbColor
from src.main.utils.time_functions import TimeFunctions


class LightingController(Controller):
	
	def __init__(self, lightingConfig: LightingConfig):
		self.lightingConfig = lightingConfig
		self._setupLeds()
		self.start_time = lightingConfig.START_TIME
		self.duration = lightingConfig.DURATION
		self.min_brightness = lightingConfig.MIN_BRIGHTNESS
		self.max_brightness = lightingConfig.MAX_BRIGHTNESS
		self.color_steps = self.generateColorSteps()
		self.enabled = False

	def start(self):
		self.enabled = True
		self.exit = threading.Event()
		if self.lightingConfig.DEMO == True:
			self.thread = threading.Thread(target=self.demo)
		else:
			self.thread = threading.Thread(target=self.realtime)
		self.thread.start()

	def stop(self):
		self.enabled = False
		self.exit.set()
		if self.led != None:
			self.led.off()

	def generateColorSteps(self):
		transitions = self.duration * 60
		return ColorFunctions.interpolateRgbGradient(self.lightingConfig.COLORS, transitions)

	def getColorForTime(self, time: datetime) -> RgbColor:
		if TimeFunctions.isTimeWithinRange(time, self.start_time, self.start_time + self.duration):
			minute_of_day = TimeFunctions.minuteOfDay(time)
			offset = (self.start_time * 60) + 1
			idx = minute_of_day - offset
			idx = clamp(idx, 0, len(self.color_steps)-1)
			return self.color_steps[idx]
		else:
			return Colors.BLACK

	def getBrightnessForTime(self, time: datetime) -> float:
		return TimeFunctions.cosineInterpolation(time, self.start_time, self.duration, self.min_brightness, self.max_brightness)

	def updateLED(self, now):
		color = self.getColorForTime(now)
		brightness = self.getBrightnessForTime(now)
		color = color.setBrightness(brightness)
		print(now, brightness, color.asPercents())
		if self.led != None:
			self.led.color = color.asPercents()

	def realtime(self):
		while not self.exit.is_set():
			now = datetime.now()
			self.updateLED(now)
			self.exit.wait(60)

	def demo(self):
		self._demoTimeRange()

	def _setupLeds(self):
		self.led = None
		if importlib_util.find_spec('gpiozero') is not None:
			from gpiozero import RGBLED
			self.led = RGBLED(self.lightingConfig.GPIO.pins[0], self.lightingConfig.GPIO.pins[1], self.lightingConfig.GPIO.pins[2], False)
			self.led.off()

	def _demoSingleColor(self):
		if self.led != None:
			self.led.color = NaturalColors.LATE_EVENING.asPercents()

	def _demoMultiColors(self):
		if self.led != None:
			colors = [NaturalColors.EVENING, NaturalColors.LATE_EVENING, NaturalColors.DUSK, NaturalColors.NIGHT]
			counter = 0
			while not self.exit.is_set():
				color = colors[counter%len(colors)]
				color_percent = color.asPercents()
				print(color.asRgb(), color_percent)
				self.led.color = color_percent
				counter+=1
				self.exit.wait(1)

	def _demoTimeRange(self):
		for h in range(self.start_time, self.start_time + self.duration):
			for m in range(0, 60):
				if not self.exit.is_set():
					now = datetime(2021, 8, 8, h, m, 0)
					self.updateLED(now)
					self.exit.wait(0.1)
