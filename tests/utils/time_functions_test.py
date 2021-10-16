import math
from datetime import datetime

from vivpi.utils.time_functions import TimeFunctions
from assert4py.annotations import skip, test
from assert4py.assertions import assertThat

@test
class TimeFunctionsTest:

	@test
	def testSecondOfDay():
		hour = 13
		minute = 14
		second = 15
		time = datetime(2021, 8, 15, hour, minute, second)
		result = TimeFunctions.secondOfDay(time)
		assertThat(result).isEqualTo(hour * 3600 + minute * 60 + second)
	
	@test
	def testMinuteOfDay():
		hour = 13
		minute = 14
		second = 15
		time = datetime(2021, 8, 15, hour, minute, second)
		result = TimeFunctions.minuteOfDay(time)
		assertThat(result).isEqualTo(hour * 60 + minute)

	@test
	def testTimeFromHours():
		time1 = TimeFunctions.timeFromHours(8.51)
		assertThat(time1.hour).isEqualTo(8)
		assertThat(time1.minute).isEqualTo(30)
		assertThat(time1.second).isEqualTo(36)

		time2 = TimeFunctions.timeFromHours(0)
		assertThat(time2.hour).isEqualTo(0)
		assertThat(time2.minute).isEqualTo(0)
		assertThat(time2.second).isEqualTo(0)

		time3 = TimeFunctions.timeFromHours(24)
		assertThat(time3.hour).isEqualTo(23)
		assertThat(time3.minute).isEqualTo(59)
		assertThat(time3.second).isEqualTo(59)

	@test
	def testWithinRange():
		start = 8
		time1 = TimeFunctions.timeFromHours(12)
		end = 16
		assertThat(TimeFunctions.isTimeWithinRange(time1, start, end)).isTrue()

		time2 = TimeFunctions.timeFromHours(6)
		assertThat(TimeFunctions.isTimeWithinRange(time2, start, end)).isFalse()

		time3 = TimeFunctions.timeFromHours(20)
		assertThat(TimeFunctions.isTimeWithinRange(time3, start, end)).isFalse()

	@skip
	def testSunriseSunset():
		pass

	@test
	def testLinearInterpolation():
		s=8
		d=14
		l=0
		h=1
		
		t_hour0 = TimeFunctions.timeFromHours(0)
		t_start = TimeFunctions.timeFromHours(s)
		t_half1 = TimeFunctions.timeFromHours(s+1*(d/4))
		t_mid = TimeFunctions.timeFromHours(s+(d/2))
		t_half2 = TimeFunctions.timeFromHours(s+3*(d/4))
		t_end = TimeFunctions.timeFromHours(s+d)
		t_hour24 = TimeFunctions.timeFromHours(24)

		hour0 = TimeFunctions.linearInterpolation(t_hour0, s, d, l, h)
		min1 = TimeFunctions.linearInterpolation(t_start, s, d, l, h)
		half1 = TimeFunctions.linearInterpolation(t_half1, s, d, l, h)
		max = TimeFunctions.linearInterpolation(t_mid, s, d, l, h)
		half2 = TimeFunctions.linearInterpolation(t_half2, s, d, l, h)
		min2 = TimeFunctions.linearInterpolation(t_end, s, d, l, h)
		hour24 = TimeFunctions.linearInterpolation(t_hour24, s, d, l, h)

		assertThat(hour0).isEqualTo(l)
		assertThat(min1).isEqualTo(l)
		assertThat(half1).isEqualTo(0.5)
		assertThat(max).isEqualTo(h)
		assertThat(half2).isEqualTo(0.5)
		assertThat(min2).isEqualTo(l)
		assertThat(hour24).isEqualTo(l)

	@test
	def testHalfSineInterpolation():
		s=8
		d=14
		l=0
		h=1

		t_hour0 = TimeFunctions.timeFromHours(0)
		t_start = TimeFunctions.timeFromHours(s)
		t_half1 = TimeFunctions.timeFromHours(s+1*(d/4))
		t_mid = TimeFunctions.timeFromHours(s+(d/2))
		t_half2 = TimeFunctions.timeFromHours(s+3*(d/4))
		t_end = TimeFunctions.timeFromHours(s+d)
		t_hour24 = TimeFunctions.timeFromHours(24)

		hour0 = TimeFunctions.halfSineInterpolation(t_hour0, s, d, l, h)
		min1 = TimeFunctions.halfSineInterpolation(t_start, s, d, l, h)
		half1 = TimeFunctions.halfSineInterpolation(t_half1, s, d, l, h)
		max = TimeFunctions.halfSineInterpolation(t_mid, s, d, l, h)
		half2 = TimeFunctions.halfSineInterpolation(t_half2, s, d, l, h)
		min2 = TimeFunctions.halfSineInterpolation(t_end, s, d, l, h)
		hour24 = TimeFunctions.halfSineInterpolation(t_hour24, s, d, l, h)

		assertThat(hour0).isEqualTo(l)
		assertThat(min1).isEqualTo(l)
		assertThat(half1).isCloseTo(math.sqrt(2)/2, 1e-9)
		assertThat(max).isEqualTo(h)
		assertThat(half2).isCloseTo(math.sqrt(2)/2, 1e-9)
		assertThat(min2).isEqualTo(l)
		assertThat(hour24).isEqualTo(l)

	@test
	def testCosineInterpolation():
		s=8
		d=14
		l=0
		h=1

		t_hour0 = TimeFunctions.timeFromHours(0)
		t_start = TimeFunctions.timeFromHours(s)
		t_half1 = TimeFunctions.timeFromHours(s+1*(d/4))
		t_mid = TimeFunctions.timeFromHours(s+(d/2))
		t_half2 = TimeFunctions.timeFromHours(s+3*(d/4))
		t_end = TimeFunctions.timeFromHours(s+d)
		t_hour24 = TimeFunctions.timeFromHours(24)

		hour0 = TimeFunctions.cosineInterpolation(t_hour0, s, d, l, h)
		min1 = TimeFunctions.cosineInterpolation(t_start, s, d, l, h)
		half1 = TimeFunctions.cosineInterpolation(t_half1, s, d, l, h)
		max = TimeFunctions.cosineInterpolation(t_mid, s, d, l, h)
		half2 = TimeFunctions.cosineInterpolation(t_half2, s, d, l, h)
		min2 = TimeFunctions.cosineInterpolation(t_end, s, d, l, h)
		hour24 = TimeFunctions.cosineInterpolation(t_hour24, s, d, l, h)

		assertThat(hour0).isEqualTo(l)
		assertThat(min1).isEqualTo(l)
		assertThat(half1).isCloseTo(0.5, 1e-9)
		assertThat(max).isEqualTo(h)
		assertThat(half2).isCloseTo(0.5, 1e-9)
		assertThat(min2).isEqualTo(l)
		assertThat(hour24).isEqualTo(l)

	@test
	def testParabolicInterpolation():
		s=8
		d=14
		l=0
		h=1
		
		t_hour0 = TimeFunctions.timeFromHours(0)
		t_start = TimeFunctions.timeFromHours(s)
		t_half1 = TimeFunctions.timeFromHours(s+1*(d/4))
		t_mid = TimeFunctions.timeFromHours(s+(d/2))
		t_half2 = TimeFunctions.timeFromHours(s+3*(d/4))
		t_end = TimeFunctions.timeFromHours(s+d)
		t_hour24 = TimeFunctions.timeFromHours(24)

		hour0 = TimeFunctions.parabolicInterpolation(t_hour0, s, d, l, h)
		min1 = TimeFunctions.parabolicInterpolation(t_start, s, d, l, h)
		half1 = TimeFunctions.parabolicInterpolation(t_half1, s, d, l, h)
		max = TimeFunctions.parabolicInterpolation(t_mid, s, d, l, h)
		half2 = TimeFunctions.parabolicInterpolation(t_half2, s, d, l, h)
		min2 = TimeFunctions.parabolicInterpolation(t_end, s, d, l, h)
		hour24 = TimeFunctions.parabolicInterpolation(t_hour24, s, d, l, h)

		assertThat(hour0).isEqualTo(l)
		assertThat(min1).isEqualTo(l)
		assertThat(half1).isEqualTo(0.75)
		assertThat(max).isEqualTo(h)
		assertThat(half2).isEqualTo(0.75)
		assertThat(min2).isEqualTo(l)
		assertThat(hour24).isEqualTo(l)
