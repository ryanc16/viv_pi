from src.main.utils.colors import Colors
from src.main.utils.rgb_color import RgbColor
from src.test.comparators.color_comparator import colorTupleComparator, rgbColorComparator
from src.test.framework.annotations import test
from src.test.framework.assertions import assertThat

@test
class RgbColorTest:

	@test
	def testAsRgb():
		color = RgbColor(127, 85, 255)
		rgb = color.asRgb()
		assertThat(rgb).isTypeOf(tuple)
		assertThat(rgb[0]).isEqualTo(127)
		assertThat(rgb[1]).isEqualTo(85)
		assertThat(rgb[2]).isEqualTo(255)

	@test
	def testAsPercents():
		color = RgbColor(127, 85, 255)
		percents = color.asPercents()
		assertThat(percents).isTypeOf(tuple)
		assertThat(percents[0]).isEqualTo(127/255)
		assertThat(percents[1]).isEqualTo(85/255)
		assertThat(percents[2]).isEqualTo(255/255)

	@test
	def testAsHex():
		color = RgbColor(127, 42, 245)
		hex = color.asHex()
		assertThat(hex).isTypeOf(str)
		assertThat(hex).isEqualTo("#7F2AF5")

	@test
	def testColorBrightness10Percent():
		result = Colors.WHITE.setBrightness(0.1)
		assertThat(result.asRgb()).isEqualTo((25.5, 25.5, 25.5))

	@test
	def testColorBrightness50Percent():
		result = Colors.WHITE.setBrightness(0.5)
		assertThat(result.asRgb()).isEqualTo((127.5, 127.5, 127.5))

	@test
	def testColorBrightness90Percent():
		result = Colors.WHITE.setBrightness(0.9)
		assertThat(result.asRgb()).isEqualTo((229.5, 229.5, 229.5))

	@test
	def testAdjustBrightness():
		assertThat(Colors.BLACK.adjust_brightness(0.5).asRgb()).isEqualTo((127.5, 127.5, 127.5))
		assertThat(Colors.BLACK.adjust_brightness(1).asRgb()).isEqualTo((255, 255, 255))
		assertThat(Colors.WHITE.adjust_brightness(-0.5).asRgb()).isEqualTo((127.5, 127.5, 127.5))
		assertThat(Colors.WHITE.adjust_brightness(-1).asRgb()).isEqualTo((0, 0, 0))

	@test
	def testColorLightness():
		result = Colors.RED.lightness(0.6)
		assertThat(result.asRgb()).whenComparedUsing(colorTupleComparator).isEqualTo((255, 51, 51))

	@test
	def testColorLighten():
		result = Colors.RED.lighten(0.1)
		assertThat(result.asRgb()).whenComparedUsing(colorTupleComparator).isEqualTo((255, 51, 51))
	
	@test
	def testColorDarken():
		result = Colors.RED.darken(0.1)
		assertThat(result.asRgb()).whenComparedUsing(colorTupleComparator).isEqualTo((204, 0, 0))

	@test
	def testColorLightnessEquality():
		assertThat(Colors.RED.lightness(0.75)).whenComparedUsing(rgbColorComparator).isEqualTo(Colors.RED.lighten(0.25))
		assertThat(Colors.RED.lightness(0.40)).whenComparedUsing(rgbColorComparator).isEqualTo(Colors.RED.darken(0.10))
