from datetime import datetime
import math

from src.main.utils.time_functions import TimeFunctions
from src.test.framework.annotations import skip, test
from src.test.framework.assertions import assertThat
from src.test.framework.test import Test


class TimeFunctionsTest(Test):

	@test
	def testSecondOfDay():
		hour = 13
		minute = 14
		second = 15
		time = datetime(2021, 8, 15, hour, minute, second)
		result = TimeFunctions.second_of_day(time)
		assertThat(result).isEqualTo(hour * 3600 + minute * 60 + second)
	
	@test
	def testMinuteOfDay():
		hour = 13
		minute = 14
		second = 15
		time = datetime(2021, 8, 15, hour, minute, second)
		result = TimeFunctions.minute_of_day(time)
		assertThat(result).isEqualTo(hour * 60 + minute)

	@test
	def testTimeFromHours():
		time1 = TimeFunctions.time_from_hours(8.51)
		assertThat(time1.hour).isEqualTo(8)
		assertThat(time1.minute).isEqualTo(30)
		assertThat(time1.second).isEqualTo(36)

		time2 = TimeFunctions.time_from_hours(0)
		assertThat(time2.hour).isEqualTo(0)
		assertThat(time2.minute).isEqualTo(0)
		assertThat(time2.second).isEqualTo(0)

		time3 = TimeFunctions.time_from_hours(24)
		assertThat(time3.hour).isEqualTo(23)
		assertThat(time3.minute).isEqualTo(59)
		assertThat(time3.second).isEqualTo(59)

	@test
	def testWithinRange():
		start = 8
		time1 = TimeFunctions.time_from_hours(12)
		end = 16
		assertThat(TimeFunctions.within_range(time1, start, end)).isTrue()

		time2 = TimeFunctions.time_from_hours(6)
		assertThat(TimeFunctions.within_range(time2, start, end)).isFalse()

		time3 = TimeFunctions.time_from_hours(20)
		assertThat(TimeFunctions.within_range(time3, start, end)).isFalse()

	@skip
	def testSunriseSunset():
		pass

	@test
	def testLinearInterpolation():
		s=8
		d=14
		l=0
		h=1
		
		t_hour0 = TimeFunctions.time_from_hours(0)
		t_start = TimeFunctions.time_from_hours(s)
		t_half1 = TimeFunctions.time_from_hours(s+1*(d/4))
		t_mid = TimeFunctions.time_from_hours(s+(d/2))
		t_half2 = TimeFunctions.time_from_hours(s+3*(d/4))
		t_end = TimeFunctions.time_from_hours(s+d)
		t_hour24 = TimeFunctions.time_from_hours(24)

		hour0 = TimeFunctions.linear_interpolation(t_hour0, s, d, l, h)
		min1 = TimeFunctions.linear_interpolation(t_start, s, d, l, h)
		half1 = TimeFunctions.linear_interpolation(t_half1, s, d, l, h)
		max = TimeFunctions.linear_interpolation(t_mid, s, d, l, h)
		half2 = TimeFunctions.linear_interpolation(t_half2, s, d, l, h)
		min2 = TimeFunctions.linear_interpolation(t_end, s, d, l, h)
		hour24 = TimeFunctions.linear_interpolation(t_hour24, s, d, l, h)

		assertThat(hour0).isEqualTo(0)
		assertThat(min1).isEqualTo(0)
		assertThat(half1).isEqualTo(0.5)
		assertThat(max).isEqualTo(1)
		assertThat(half2).isEqualTo(0.5)
		assertThat(min2).isEqualTo(0)
		assertThat(hour24).isEqualTo(0)

	@test
	def testHalfSineInterpolation():
		s=8
		d=14
		l=0
		h=1

		t_hour0 = TimeFunctions.time_from_hours(0)
		t_start = TimeFunctions.time_from_hours(s)
		t_half1 = TimeFunctions.time_from_hours(s+1*(d/4))
		t_mid = TimeFunctions.time_from_hours(s+(d/2))
		t_half2 = TimeFunctions.time_from_hours(s+3*(d/4))
		t_end = TimeFunctions.time_from_hours(s+d)
		t_hour24 = TimeFunctions.time_from_hours(24)

		hour0 = TimeFunctions.half_sine_interpolation(t_hour0, s, d, l, h)
		min1 = TimeFunctions.half_sine_interpolation(t_start, s, d, l, h)
		half1 = TimeFunctions.half_sine_interpolation(t_half1, s, d, l, h)
		max = TimeFunctions.half_sine_interpolation(t_mid, s, d, l, h)
		half2 = TimeFunctions.half_sine_interpolation(t_half2, s, d, l, h)
		min2 = TimeFunctions.half_sine_interpolation(t_end, s, d, l, h)
		hour24 = TimeFunctions.half_sine_interpolation(t_hour24, s, d, l, h)

		assertThat(hour0).isEqualTo(0)
		assertThat(min1).isEqualTo(0)
		assertThat(half1).isCloseTo(math.sqrt(2)/2, 1e-9)
		assertThat(max).isEqualTo(1)
		assertThat(half2).isCloseTo(math.sqrt(2)/2, 1e-9)
		assertThat(min2).isEqualTo(0)
		assertThat(hour24).isEqualTo(0)

	@test
	def testCosineInterpolation():
		s=8
		d=14
		l=0
		h=1

		t_hour0 = TimeFunctions.time_from_hours(0)
		t_start = TimeFunctions.time_from_hours(s)
		t_half1 = TimeFunctions.time_from_hours(s+1*(d/4))
		t_mid = TimeFunctions.time_from_hours(s+(d/2))
		t_half2 = TimeFunctions.time_from_hours(s+3*(d/4))
		t_end = TimeFunctions.time_from_hours(s+d)
		t_hour24 = TimeFunctions.time_from_hours(24)

		hour0 = TimeFunctions.cosine_interpolation(t_hour0, s, d, l, h)
		min1 = TimeFunctions.cosine_interpolation(t_start, s, d, l, h)
		half1 = TimeFunctions.cosine_interpolation(t_half1, s, d, l, h)
		max = TimeFunctions.cosine_interpolation(t_mid, s, d, l, h)
		half2 = TimeFunctions.cosine_interpolation(t_half2, s, d, l, h)
		min2 = TimeFunctions.cosine_interpolation(t_end, s, d, l, h)
		hour24 = TimeFunctions.cosine_interpolation(t_hour24, s, d, l, h)

		assertThat(hour0).isEqualTo(0)
		assertThat(min1).isEqualTo(0)
		assertThat(half1).isCloseTo(0.5, 1e-9)
		assertThat(max).isEqualTo(1)
		assertThat(half2).isCloseTo(0.5, 1e-9)
		assertThat(min2).isEqualTo(0)
		assertThat(hour24).isEqualTo(0)

	@test
	def testParabolicInterpolation():
		s=8
		d=14
		l=0
		h=1
		
		t_hour0 = TimeFunctions.time_from_hours(0)
		t_start = TimeFunctions.time_from_hours(s)
		t_half1 = TimeFunctions.time_from_hours(s+1*(d/4))
		t_mid = TimeFunctions.time_from_hours(s+(d/2))
		t_half2 = TimeFunctions.time_from_hours(s+3*(d/4))
		t_end = TimeFunctions.time_from_hours(s+d)
		t_hour24 = TimeFunctions.time_from_hours(24)

		hour0 = TimeFunctions.parabolic_interpolation(t_hour0, s, d, l, h)
		min1 = TimeFunctions.parabolic_interpolation(t_start, s, d, l, h)
		half1 = TimeFunctions.parabolic_interpolation(t_half1, s, d, l, h)
		max = TimeFunctions.parabolic_interpolation(t_mid, s, d, l, h)
		half2 = TimeFunctions.parabolic_interpolation(t_half2, s, d, l, h)
		min2 = TimeFunctions.parabolic_interpolation(t_end, s, d, l, h)
		hour24 = TimeFunctions.parabolic_interpolation(t_hour24, s, d, l, h)

		assertThat(hour0).isEqualTo(0)
		assertThat(min1).isEqualTo(0)
		assertThat(half1).isEqualTo(0.75)
		assertThat(max).isEqualTo(1)
		assertThat(half2).isEqualTo(0.75)
		assertThat(min2).isEqualTo(0)
		assertThat(hour24).isEqualTo(0)
