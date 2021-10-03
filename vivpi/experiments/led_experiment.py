from gpiozero import PWMLED
from time import sleep
from datetime import datetime
import math
"""
useful tools:
gpiozero docs
https://gpiozero.readthedocs.io/en/stable/api_output.html#pwmled
interactive graphing
https://www.desmos.com/calculator
"""

led = PWMLED(26)
START_TIME = 8
DURATION = 14
MIN_BRIGHTNESS = 0.1
MAX_BRIGHTNESS = 1

def main():
	prog_demo()

def prog_demo():
	for h in range(0,24):
		for m in range(0,60):
			now = datetime(2021, 8, 8, h, m, 0)
			brightness = get_brightness_for_time(now)
			led.value = brightness
			print(str(now) + " = " + str(round(brightness*100, 2)) + "% brightness", end='\r')
			sleep(0.05)

def prog_time_based():
	while True:
		now = datetime.now()
		brightness = get_brightness_for_time(now)
		led.value = brightness
		print(str(now) + " = " + str(brightness*100) + "% brightness")
		sleep(1)

def get_brightness_for_time(time):
	seconds_elapsed_today = (time.hour * 3600) + (time.minute * 60) + time.second
	return max(0, sine_interpolation(START_TIME, DURATION, MIN_BRIGHTNESS, MAX_BRIGHTNESS, seconds_elapsed_today))
	# return linear_interpolation(START_TIME, DURATION, MIN_BRIGHTNESS, MAX_BRIGHTNESS, seconds_elapsed_today)

def linear_interpolation(start_time_hr, duration, min_brightness, max_brightness, now):
	# y = mx + b
	b = start_time_hr * 3600 # shift left and right
	m = duration * 3600 #1:24 increase/decrease the slope
	c = min_brightness #0:1 raise up and down
	d = max_brightness #0:1
	x = now
	if (x >= b and x <= (b + m)):
		if (x < (b + (m/2))):
			return (1 / m) * x - (b * (1 / m)) + c
		else:
			return 1 - ((1 / m) * x - (b * (1 / m)) + c)
	else:
		return min_brightness



def sine_interpolation(start_time_hr, duration, min_brightness, max_brightness, now):
	# y = a * sin(b * (x - d)) + c
	d = start_time_hr * 3600 #0:24 shift left and right
	b = duration * 3600 #1:24 increase/decrease the frequency
	c = min_brightness #0:1 raise up and down
	a = max_brightness - min_brightness #0:1 increase/decrease the amplitude 
	x = now
	if (x >= d and x <= (d + b)):
		return a * math.sin((math.pi / b) * (x - d)) + c
	else:
		return min_brightness

main()