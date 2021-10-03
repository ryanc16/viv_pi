from vivpi.utils.color_functions import ColorFunctions
from vivpi.utils.colors import Colors
from tests.comparators.color_comparator import colorTupleComparator
from assert4py.annotations import test
from assert4py.assertions import assertThat

@test
class ColorFunctionsTest:

	@test
	def testColorBlending():
		startColor = Colors.WHITE
		endColor = Colors.YELLOW
		result = ColorFunctions.blendColors(startColor, endColor, 0.5)
		assertThat(result.asRgb()).isEqualTo((255, 167.5, 127.5))

	@test
	def testColorInterpolation():
		result = ColorFunctions.interpolateRgb(Colors.BLACK, Colors.WHITE, 10)
		# 11 because a color is added for each fractional blending amount from 0%-100% (n+1 iterations)
		assertThat(result).hasLengthOf(11)
		assertThat(result[0].asRgb()).whenComparedUsing(colorTupleComparator).isEqualTo((0, 0, 0))
		assertThat(result[5].asRgb()).whenComparedUsing(colorTupleComparator).isEqualTo((127.5, 127.5, 127.5))
		assertThat(result[10].asRgb()).whenComparedUsing(colorTupleComparator).isEqualTo((255, 255, 255))

	@test
	def testColorInterpolationGradient():
		result = ColorFunctions.interpolateRgbGradient([Colors.BLACK, Colors.RED, Colors.WHITE], 100)
		# 102 because a color is added for each fractional blending amount for each color from 0%-100% (n+1 iterations)
		assertThat(result).hasLengthOf(100)
		assertThat(result[0].asRgb()).whenComparedUsing(colorTupleComparator).isEqualTo((0, 0, 0))
		assertThat(result[49].asRgb()).whenComparedUsing(colorTupleComparator).isEqualTo((255, 0, 0))
		assertThat(result[99].asRgb()).whenComparedUsing(colorTupleComparator).isEqualTo((255, 255, 255))
