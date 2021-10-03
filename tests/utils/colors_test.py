from vivpi.utils.colors import Colors
from vivpi.utils.rgb_color import RgbColor
from assert4py.annotations import test
from assert4py.assertions import assertThat


@test
class ColorsTest:

	@test
	def testWhiteColor():
		assertThat(Colors.WHITE).isInstanceOf(RgbColor)
		assertThat(Colors.WHITE.r).isEqualTo(255)
		assertThat(Colors.WHITE.g).isEqualTo(255)
		assertThat(Colors.WHITE.b).isEqualTo(255)

	@test
	def testGrayColor():
		assertThat(Colors.GRAY).isInstanceOf(RgbColor)
		assertThat(Colors.GRAY.r).isEqualTo(127)
		assertThat(Colors.GRAY.g).isEqualTo(127)
		assertThat(Colors.GRAY.b).isEqualTo(127)

	@test
	def testBlackColor():
		assertThat(Colors.BLACK).isInstanceOf(RgbColor)
		assertThat(Colors.BLACK.r).isEqualTo(0)
		assertThat(Colors.BLACK.g).isEqualTo(0)
		assertThat(Colors.BLACK.b).isEqualTo(0)

	@test
	def testRedColor():
		assertThat(Colors.RED).isInstanceOf(RgbColor)
		assertThat(Colors.RED.r).isEqualTo(255)
		assertThat(Colors.RED.g).isEqualTo(0)
		assertThat(Colors.RED.b).isEqualTo(0)

	@test
	def testOrangeColor():
		assertThat(Colors.ORANGE).isInstanceOf(RgbColor)
		assertThat(Colors.ORANGE.r).isEqualTo(255)
		assertThat(Colors.ORANGE.g).isEqualTo(30)
		assertThat(Colors.ORANGE.b).isEqualTo(0)

	@test
	def testYellowColor():
		assertThat(Colors.YELLOW).isInstanceOf(RgbColor)
		assertThat(Colors.YELLOW.r).isEqualTo(255)
		assertThat(Colors.YELLOW.g).isEqualTo(80)
		assertThat(Colors.YELLOW.b).isEqualTo(0)

	@test
	def testGreenColor():
		assertThat(Colors.GREEN).isInstanceOf(RgbColor)
		assertThat(Colors.GREEN.r).isEqualTo(0)
		assertThat(Colors.GREEN.g).isEqualTo(255)
		assertThat(Colors.GREEN.b).isEqualTo(0)

	@test
	def testCyanColor():
		assertThat(Colors.CYAN).isInstanceOf(RgbColor)
		assertThat(Colors.CYAN.r).isEqualTo(0)
		assertThat(Colors.CYAN.g).isEqualTo(165)
		assertThat(Colors.CYAN.b).isEqualTo(255)

	@test
	def testBlueColor():
		assertThat(Colors.BLUE).isInstanceOf(RgbColor)
		assertThat(Colors.BLUE.r).isEqualTo(0)
		assertThat(Colors.BLUE.g).isEqualTo(0)
		assertThat(Colors.BLUE.b).isEqualTo(255)

	@test
	def testPurpleColor():
		assertThat(Colors.PURPLE).isInstanceOf(RgbColor)
		assertThat(Colors.PURPLE.r).isEqualTo(80)
		assertThat(Colors.PURPLE.g).isEqualTo(0)
		assertThat(Colors.PURPLE.b).isEqualTo(255)

	@test
	def testMagentaColor():
		assertThat(Colors.MAGENTA).isInstanceOf(RgbColor)
		assertThat(Colors.MAGENTA.r).isEqualTo(255)
		assertThat(Colors.MAGENTA.g).isEqualTo(0)
		assertThat(Colors.MAGENTA.b).isEqualTo(30)

	@test
	def testColorsToList():
		assertThat(Colors.toList()).isInstanceOf(list)
		assertThat(Colors.toList()).hasLengthOf(11)
		expected = [
			Colors.WHITE,
			Colors.GRAY,
			Colors.BLACK,
			Colors.RED,
			Colors.ORANGE,
			Colors.YELLOW,
			Colors.GREEN,
			Colors.CYAN,
			Colors.BLUE,
			Colors.PURPLE,
			Colors.MAGENTA
		]
		assertThat(Colors.toList()).contains(expected)
