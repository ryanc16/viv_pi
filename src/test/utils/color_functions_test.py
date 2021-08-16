from src.main.utils.color_functions import ColorFunctions
from src.main.utils.colors import Colors
from src.test.comparators.color_comparator import colorTupleComparator
from src.test.framework.annotations import test
from src.test.framework.assertions import assertThat
from src.test.framework.test import Test


class ColorFunctionsTest(Test):

	@test
	def testColorBlending():
		startColor = Colors.WHITE
		endColor = Colors.YELLOW
		result = ColorFunctions.blend_colors(startColor, endColor, 0.5)
		assertThat(result.as_rgb()).isEqualTo((255, 167.5, 127.5))

	@test
	def testColorInterpolation():
		result = ColorFunctions.interpolate_rgb(Colors.BLACK, Colors.WHITE, 10)
		# 11 because a color is added for each fractional blending amount from 0%-100% (n+1 iterations)
		assertThat(result).hasLengthOf(11)
		assertThat(result[0].as_rgb()).whenComparedUsing(colorTupleComparator).isEqualTo((0, 0, 0))
		assertThat(result[5].as_rgb()).whenComparedUsing(colorTupleComparator).isEqualTo((127.5, 127.5, 127.5))
		assertThat(result[10].as_rgb()).whenComparedUsing(colorTupleComparator).isEqualTo((255, 255, 255))

	@test
	def testColorInterpolationGradient():
		result = ColorFunctions.interpolate_rgb_gradient([Colors.BLACK, Colors.RED, Colors.WHITE], 100)
		# 102 because a color is added for each fractional blending amount for each color from 0%-100% (n+1 iterations)
		assertThat(result).hasLengthOf(102)
		assertThat(result[0].as_rgb()).whenComparedUsing(colorTupleComparator).isEqualTo((0, 0, 0))
		assertThat(result[50].as_rgb()).whenComparedUsing(colorTupleComparator).isEqualTo((255, 0, 0))
		assertThat(result[101].as_rgb()).whenComparedUsing(colorTupleComparator).isEqualTo((255, 255, 255))
