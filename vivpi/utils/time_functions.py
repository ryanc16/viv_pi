from datetime import datetime
import math

from vivpi.utils.clamp import clamp
class TimeFunctions:

	def secondOfDay(time) -> float:
		return (time.hour * 3600) + (time.minute * 60) + time.second

	def minuteOfDay(time) -> float:
		return (time.hour * 60) + time.minute

	def timeFromHours(hrs: float) -> datetime:
		hr = math.floor(hrs)
		hr = clamp(hr, 0, 23)
		min = math.floor((hrs-hr)*60)
		min = clamp(min, 0, 59)
		sec = round((((hrs-hr)*60)-min)*60)
		sec = clamp(sec, 0, 59)
		return datetime.now().replace(hour=hr, minute=min, second=sec, microsecond=0)

	def isTimeWithinRange(time: datetime, start_time_hr: float, stop_time_hr: float) -> bool:
		return time >= TimeFunctions.timeFromHours(start_time_hr) and time <= TimeFunctions.timeFromHours(stop_time_hr)

	def linearInterpolation(time: datetime, start_time_hr: float, duration: float, min_brightness: float, max_brightness: float) -> float:
		"""
		Parameters
		----------
		time: datetime
			The datetime of interest to determine the brightness level for
		start_time_hr : float
			The start time in the day in terms of hours. Valid values are from 0 to 24
		duration : float
			The duration of the light on time during the day. Value values are from 0 to 24
		min_brightness : float
			The minimum brightness value, which will be used as the starting value when current time is
			start_time_hr, and when current time is start_time_hr + duration, or outside those bounds.
		max_brightness: float
			the maximum brightness value, which will be reached at the midpoint (peak) of the duration, so start_time_hr + (duration/2)
		
		Returns
		-------
		float
			The brightness level from 0 to 1 for the provided time, given the parameters
		"""
		#					|(h - l)(d + 2s - 2x)|
		#	y = h - |--------------------|
		#					|					2					 |
		s = start_time_hr * 3600 #0:24 shift left and right
		d = duration * 3600 #1:24 increase/decrease the slope
		l = min_brightness #0:1 raise up and down
		h = max_brightness #0:1
		x = TimeFunctions.secondOfDay(time)
		
		if (x > s and x < (s + d)):
			return h - abs(((h - l) * (d + (2 * s) - (2 * x))) / d)
		else:
			return min_brightness

	def halfSineInterpolation(time: datetime, start_time_hr: float, duration: float, min_brightness: float, max_brightness: float) -> float:
		"""
		Parameters
		----------
		time: datetime
			The datetime of interest to determine the brightness level for
		start_time_hr : float
			The start time in the day in terms of hours. Valid values are from 0 to 24
		duration : float
			The duration of the light on time during the day. Value values are from 0 to 24
		min_brightness : float
			The minimum brightness value, which will be used as the starting value when current time is
			start_time_hr, and when current time is start_time_hr + duration, or outside those bounds.
		max_brightness: float
			the maximum brightness value, which will be reached at the midpoint (peak) of the duration, so start_time_hr + (duration/2)
		
		Returns
		-------
		float
			The brightness level from 0 to 1 for the provided time, given the parameters
		"""
		#											pi
		#	y = (h - l) * sin(------ * (x - s)) + l
		#											d
		s = start_time_hr * 3600 #0:24 shift left and right
		d = duration * 3600 #1:24 increase/decrease the frequency
		l = min_brightness #0:1 raise up and down
		h = max_brightness #0:1 increase/decrease the amplitude 
		x = TimeFunctions.secondOfDay(time)

		if (x > s and x < (s + d)):
			return (h - l) * math.sin((math.pi / d) * (x - s)) + l
		else:
			return min_brightness

	def cosineInterpolation(time: datetime, start_time_hr: float, duration: float, min_brightness: float, max_brightness: float) -> float:
		"""
		Parameters
		----------
		time: datetime
			The datetime of interest to determine the brightness level for
		start_time_hr : float
			The start time in the day in terms of hours. Valid values are from 0 to 24
		duration : float
			The duration of the light on time during the day. Value values are from 0 to 24
		min_brightness : float
			The minimum brightness value, which will be used as the starting value when current time is
			start_time_hr, and when current time is start_time_hr + duration, or outside those bounds.
		max_brightness: float
			the maximum brightness value, which will be reached at the midpoint (peak) of the duration, so start_time_hr + (duration/2)
		
		Returns
		-------
		float
			The brightness level from 0 to 1 for the provided time, given the parameters
		"""
		#			 1										2pi(s-x)
		#	y = --- * ((l - h) *	cos(--------) + h + l)
		#			 2											 d
		s = start_time_hr * 3600
		d = duration * 3600
		l = min_brightness
		h = max_brightness
		x = TimeFunctions.secondOfDay(time)

		if (x > s and x < (s + d)):
			return 0.5 * ((l - h) * math.cos((2 * math.pi * (s - x)) / d) + h + l)
		else:
			return min_brightness
	
	def parabolicInterpolation(time: datetime, start_time_hr: float, duration: float, min_brightness: float, max_brightness: float) -> float:
		"""
		Parameters
		----------
		time: datetime
			The datetime of interest to determine the brightness level for
		start_time_hr : float
			The start time in the day in terms of hours. Valid values are from 0 to 24
		duration : float
			The duration of the light on time during the day. Value values are from 0 to 24
		min_brightness : float
			The minimum brightness value, which will be used as the starting value when current time is
			start_time_hr, and when current time is start_time_hr + duration, or outside those bounds.
		max_brightness: float
			the maximum brightness value, which will be reached at the midpoint (peak) of the duration, so start_time_hr + (duration/2)
		
		Returns
		-------
		float
			The brightness level from 0 to 1 for the provided time, given the parameters
		"""
		#					(h - l) * (d + 2s + 2x)^2
		#	y = h - -------------------------
		#										d^2
		s = start_time_hr * 3600
		d = duration * 3600
		l = min_brightness
		h = max_brightness
		x = TimeFunctions.secondOfDay(time)

		if (x > s and x < (s + d)):
			return h - ((h - l) * math.pow((d + (2 * s) - (2 * x)), 2)) / math.pow(d, 2)
		else:
			return min_brightness
