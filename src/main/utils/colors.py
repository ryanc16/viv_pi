from src.main.utils.rgb_color import RgbColor

class Colors:
	WHITE = RgbColor(255, 255, 255)
	GRAY = RgbColor(127, 127, 127)
	BLACK = RgbColor(0, 0 , 0)
	RED = RgbColor(255, 0, 0)
	ORANGE = RgbColor(255, 30, 0)
	YELLOW = RgbColor(255, 80, 0)
	GREEN = RgbColor(0, 255, 0)
	CYAN = RgbColor(0, 165, 255)
	BLUE = RgbColor(0, 0, 255)
	PURPLE = RgbColor(80, 0, 255)
	MAGENTA = RgbColor(255, 0, 30)
	
	def toList():
		return [
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