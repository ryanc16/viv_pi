from gpiozero import RGBLED
from time import sleep
import colorsys

led = RGBLED(26, 19, 13, False)

def main():
	color_steps = interpolate_rgb(Colors.YELLOW, Colors.RED, 3600)
	for i in range(0, len(color_steps)):
		color = color_steps[i]
		# color = darken(color, (i/60))
		color = from_rgb(color)
		print(color)
		led.color = color
		sleep(1)

def from_rgb(rgb_color):
	max = 255
	scale = (max/255)
	r = scale * rgb_color[0]
	g = scale * rgb_color[1]
	b = scale * rgb_color[2]
	return (r/255, g/255, b/255)

def interpolate_rgb(startcolor, goalcolor, steps):
	"""
	Take two RGB color sets and mix them over a specified number of steps.  Return the list
	"""
	# white

	R = startcolor[0]
	G = startcolor[1]
	B = startcolor[2]

	targetR = goalcolor[0]
	targetG = goalcolor[1]
	targetB = goalcolor[2]

	DiffR = targetR - R
	DiffG = targetG - G
	DiffB = targetB - B

	buffer = []

	for i in range(0, steps +1):
		iR = R + (DiffR * i / steps)
		iG = G + (DiffG * i / steps)
		iB = B + (DiffB * i / steps)

		# hR = str.replace(hex(iR), "0x", "")
		# hG = str.replace(hex(iG), "0x", "")
		# hB = str.replace(hex(iB), "0x", "")

		# if len(hR) == 1:
		# 	hR = "0" + hR
		# if len(hB) == 1:
		# 	hB = "0" + hB

		# if len(hG) == 1:
		# 	hG = "0" + hG

		# color = str.upper("#"+hR+hG+hB)
		color = (iR, iG, iB)
		buffer.append(color)

	return buffer

def darken_to(rgb, percent):
	hls = colorsys.rgb_to_hls(rgb[0], rgb[1], rgb[2])
	lightness = max(percent, 0)
	return colorsys.hls_to_rgb(hls[0], lightness, hls[2])

def darken(rgb, percent):
	hls = colorsys.rgb_to_hls(rgb[0], rgb[1], rgb[2])
	lightness = hls[1] - (hls[1] * percent)
	lightness = max(lightness, 0)
	print("lightness: " + str(lightness))
	return colorsys.hls_to_rgb(hls[0], lightness, hls[2])

def brighten_to(rgb, percent):
	print('brightening to: ' + str(percent))
	hls = colorsys.rgb_to_hls(rgb[0], rgb[1], rgb[2])
	lightness = min(percent, 1)
	return colorsys.hls_to_rgb(hls[1], lightness, hls[2])

def brighten(rgb, percent):
	hls = colorsys.rgb_to_hls(rgb[0], rgb[1], rgb[2])
	lightness = hls[1] + (hls[1] * percent)
	lightness = min(lightness, 1)
	return colorsys.hls_to_rgb(hls[1], lightness, hls[2])

class Colors:
	WHITE = (255, 255, 255)
	BLACK = (0, 0 , 0)
	RED = (255, 0, 0)
	ORANGE = (255, 30, 0)
	YELLOW = (255, 80, 0)
	GREEN = (255, 255, 0)
	CYAN = (0, 165, 255)
	BLUE = (0, 0, 255)
	PURPLE = (80, 0, 255)
	MAGENTA = (255, 0, 30)
	def toList():
		return [
			Colors.RED,
			Colors.ORANGE,
			Colors.YELLOW,
			Colors.GREEN,
			Colors.CYAN,
			Colors.BLUE,
			Colors.PURPLE,
			Colors.MAGENTA
		]

main()
