from datetime import datetime
from time import sleep

from gpiozero import RGBLED
from main.utils.rgb_color import RgbColor
from src.main.utils.color_functions import ColorFunctions
from src.main.utils.colors import Colors
from src.main.utils.time_functions import TimeFunctions

led = RGBLED(26, 19, 13, False)
START_TIME = 6
DURATION = 14
MIN_BRIGHTNESS = 0
MAX_BRIGHTNESS = 1

DAWN = ColorFunctions.blend_colors(Colors.GRAY, Colors.CYAN, 0.25).brightness(0.05)
MIDDAY = ColorFunctions.blend_colors(Colors.WHITE, Colors.YELLOW, 0.7)
EARLY_EVENING = Colors.YELLOW.lighten(0.05).adjust_brightness(+0.1)
LATE_EVENING = Colors.ORANGE.lighten(0.05).brightness(0.25)
EVENING = ColorFunctions.blend_colors(EARLY_EVENING, LATE_EVENING, 0.5)
DUSK = ColorFunctions.blend_colors(Colors.ORANGE.lighten(0.05), Colors.BLUE.lightness(0.3), 0.5).brightness(0.15)
NIGHT = Colors.BLUE.lightness(0.55).brightness(0.005)
TEST = LATE_EVENING

COLOR_STEPS = [DAWN, MIDDAY, MIDDAY, MIDDAY, MIDDAY, EVENING, DUSK, NIGHT]
#             08:00  09:45   11:30   13:15   15:00   16:45    18:30 20:15

def main():
	realtime()

def generateColorSteps():
	global COLOR_STEPS
	COLOR_STEPS = ColorFunctions.interpolate_rgb_gradient(COLOR_STEPS, DURATION*60)

def getColorForTime(time: datetime) -> RgbColor:
	minute_of_day = TimeFunctions.minute_of_day(time)
	offset = START_TIME*60
	return COLOR_STEPS[minute_of_day-offset]

def demo_single():
	led.color = TEST.as_percents()
	while True:
		sleep(1)

def demo_colors():
	colors = [EVENING, LATE_EVENING, DUSK, NIGHT]
	counter = 0
	while True:
		color = colors[counter%len(colors)]
		color_percent = color.as_percents()
		print(color.as_rgb(), color_percent)
		led.color = color_percent
		counter+=1
		sleep(1)

def demo():
	generateColorSteps()
	for h in range(START_TIME,START_TIME+DURATION):
		for m in range(0,60):
			now = datetime(2021, 8, 8, h, m, 0)
			updateLED(now)
			sleep(0.1)

def realtime():
	generateColorSteps()
	while True:
		now = datetime.now()
		updateLED(now)
		sleep(60)

def updateLED(now):
	brightness = 0
	color = Colors.BLACK
	if TimeFunctions.within_range(now, START_TIME, START_TIME+DURATION):
	# if (second_of_day-offset > 0 and second_of_day-offset < len(COLOR_STEPS)):
		brightness = TimeFunctions.cosine_interpolation(now, START_TIME, DURATION, MIN_BRIGHTNESS, MAX_BRIGHTNESS)
		color = getColorForTime(now).brightness(brightness)
	print(now, brightness, color.as_percents())
	led.color = color.as_percents()

main()
