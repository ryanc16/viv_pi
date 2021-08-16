from src.main.utils.colors import Colors
from src.main.utils.rgb_color import RgbColor
from src.test.comparators.color_comparator import colorTupleComparator
from src.test.framework.annotations import test
from src.test.framework.assertions import assertThat
from src.test.framework.test import Test


class RgbColorTest(Test):

	@test
	def testAsRgb():
		color = RgbColor(127, 85, 255)
		rgb = color.as_rgb()
		assertThat(rgb).isTypeOf(tuple)
		assertThat(rgb[0]).isEqualTo(127)
		assertThat(rgb[1]).isEqualTo(85)
		assertThat(rgb[2]).isEqualTo(255)

	@test
	def testAsPercents():
		color = RgbColor(127, 85, 255)
		percents = color.as_percents()
		assertThat(percents).isTypeOf(tuple)
		assertThat(percents[0]).isEqualTo(127/255)
		assertThat(percents[1]).isEqualTo(85/255)
		assertThat(percents[2]).isEqualTo(255/255)

	@test
	def testAsHex():
		color = RgbColor(127, 42, 245)
		hex = color.as_hex()
		assertThat(hex).isTypeOf(str)
		assertThat(hex).isEqualTo("#7F2AF5")

	@test
	def testColorBrightness10Percent():
		result = Colors.WHITE.brightness(0.1)
		assertThat(result.as_rgb()).isEqualTo((25.5, 25.5, 25.5))

	@test
	def testColorBrightness50Percent():
		result = Colors.WHITE.brightness(0.5)
		assertThat(result.as_rgb()).isEqualTo((127.5, 127.5, 127.5))

	@test
	def testColorBrightness90Percent():
		result = Colors.WHITE.brightness(0.9)
		assertThat(result.as_rgb()).isEqualTo((229.5, 229.5, 229.5))

	@test
	def testAdjustBrightness():
		assertThat(Colors.BLACK.adjust_brightness(0.5).as_rgb()).isEqualTo((127.5, 127.5, 127.5))
		assertThat(Colors.BLACK.adjust_brightness(1).as_rgb()).isEqualTo((255, 255, 255))
		assertThat(Colors.WHITE.adjust_brightness(-0.5).as_rgb()).isEqualTo((127.5, 127.5, 127.5))
		assertThat(Colors.WHITE.adjust_brightness(-1).as_rgb()).isEqualTo((0, 0, 0))

	@test
	def testColorLightness():
		result = Colors.RED.lightness(0.6)
		assertThat(result.as_rgb()).whenComparedUsing(colorTupleComparator).isEqualTo((255, 51, 51))

	@test
	def testColorLighten():
		result = Colors.RED.lighten(0.1)
		assertThat(result.as_rgb()).whenComparedUsing(colorTupleComparator).isEqualTo((255, 51, 51))
	
	@test
	def testColorDarken():
		result = Colors.RED.darken(0.1)
		assertThat(result.as_rgb()).whenComparedUsing(colorTupleComparator).isEqualTo((204, 0, 0))

	@test
	def testColorLightnessEquality():
		assertThat(Colors.RED.lightness(0.75).as_rgb()).whenComparedUsing(colorTupleComparator).isEqualTo(Colors.RED.lighten(0.25).as_rgb())
		assertThat(Colors.RED.lightness(0.40).as_rgb()).whenComparedUsing(colorTupleComparator).isEqualTo(Colors.RED.darken(0.10).as_rgb())
