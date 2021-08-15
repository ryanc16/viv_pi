import math

class TimeFunctions:

	def second_of_day(time):
		return (time.hour * 3600) + (time.minute * 60) + time.second

	def minute_of_day(time):
		return (time.hour * 60) + time.minute
	
	def get_brightness_for_time(start_time, duration, min_brightness, max_brightness, time):
		seconds_elapsed_today = TimeFunctions.second_of_day(time)
		return max(0, TimeFunctions.cosine_interpolation(start_time, duration, min_brightness, max_brightness, seconds_elapsed_today))

	def linear_interpolation(start_time_hr, duration, min_brightness, max_brightness, time):
		"""
						|(h - l)(d + 2s - 2x)|
		y = h - |--------------------|
						|					2					 |
		"""
		s = start_time_hr * 3600 #0:24 shift left and right
		d = duration * 3600 #1:24 increase/decrease the slope
		l = min_brightness #0:1 raise up and down
		h = max_brightness #0:1
		x = time
		
		if (x >= s and x <= (s + d)):
			return h - abs(((h - l) * (d + (2 * s) - (2 * x))) / d)
		else:
			return min_brightness

	def half_sine_interpolation(start_time_hr, duration, min_brightness, max_brightness, time):
		"""
											 pi
		y = (h - l) * sin(---- * (x - s)) + l
											 d
		"""
		s = start_time_hr * 3600 #0:24 shift left and right
		d = duration * 3600 #1:24 increase/decrease the frequency
		l = min_brightness #0:1 raise up and down
		h = max_brightness #0:1 increase/decrease the amplitude 
		x = time
		if (x >= s and x <= (s + d)):
			return (h - l) * math.sin((math.pi / d) * (x - s)) + l
		else:
			return min_brightness

	def cosine_interpolation(start_time_hr, duration, min_brightness, max_brightness, time):
		"""
				 1										2pi(s-x)
		y = --- * ((l - h) *	cos(--------) + h + l)
				 2											 d
		"""
		s = start_time_hr * 3600
		d = duration * 3600
		l = min_brightness
		h = max_brightness
		x = time

		if (x >= s and x <= (s + d)):
			return 0.5 * ((l - h) * math.cos((2 * math.pi * (s - x)) / d) + h + l)
		else:
			return min_brightness
	
	def parabolic_interpolation(start_time_hr, duration, min_brightness, max_brightness, time):
		"""
						(h - l) * (d + 2s + 2x)^2
		y = h - -------------------------
										d^2
		"""
		s = start_time_hr * 3600
		d = duration * 3600
		l = min_brightness
		h = max_brightness
		x = time

		if (x >= s and x <= (s + d)):
			return h - ((h - l) * math.pow((d + (2 * s) - (2 * x)), 2)) / math.pow(d, 2)
		else:
			return min_brightness
