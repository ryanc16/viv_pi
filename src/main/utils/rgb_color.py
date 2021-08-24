import colorsys
from src.main.utils.clamp import clamp

class RgbColor:
	"""
	RGB Color
	"""
	def __init__(self, r=0, g=0, b=0):
		if type(r) is tuple:
			self.r = r[0]
			self.g = r[1]
			self.b = r[2]
		else:
			self.r = r
			self.g = g
			self.b = b

	def __str__(self):
		return f"RgbColor({self.r}, {self.g}, {self.b})"

	def asPercents(self) -> tuple:
		max = 255
		scale = (max/255)
		r = scale * self.r
		g = scale * self.g
		b = scale * self.b
		return (r/255, g/255, b/255)
	
	def asRgb(self) -> tuple:
		return (self.r, self.g, self.b)

	def asHex(self) -> str:
		hR = str.replace(hex(self.r), "0x", "")
		hG = str.replace(hex(self.g), "0x", "")
		hB = str.replace(hex(self.b), "0x", "")

		if len(hR) == 1:
			hR = "0" + hR
		if len(hB) == 1:
			hB = "0" + hB
		if len(hG) == 1:
			hG = "0" + hG

		color = str.upper("#"+hR+hG+hB)
		return color

	def lightness(self, percent: float):
		rgb = self.asPercents()
		hls = colorsys.rgb_to_hls(rgb[0], rgb[1], rgb[2])
		lightness = clamp(percent, 0, 1)
		newrgb = colorsys.hls_to_rgb(hls[0], lightness, hls[2])
		return RgbColor(tuple(255*x for x in newrgb))

	def lighten(self, percentage: float):
		rgb = self.asPercents()
		hls = colorsys.rgb_to_hls(rgb[0], rgb[1], rgb[2])
		percent = clamp(percentage, 0, 1)
		lightness = hls[1] + percent
		lightness = clamp(lightness, 0, 1)
		newrgb = colorsys.hls_to_rgb(hls[0], lightness, hls[2])
		return RgbColor(tuple(255*x for x in newrgb))

	def darken(self, percentage: float):
		rgb = self.asPercents()
		hls = colorsys.rgb_to_hls(rgb[0], rgb[1], rgb[2])
		percent = clamp(percentage, 0, 1)
		lightness = hls[1] - percent
		lightness = clamp(lightness, 0, 1)
		newrgb = colorsys.hls_to_rgb(hls[0], lightness, hls[2])
		return RgbColor(tuple(255*x for x in newrgb))

	def adjust_brightness(self, percentage:float):
		rgb = self.asPercents()
		hsv = colorsys.rgb_to_hsv(rgb[0], rgb[1], rgb[2])
		percent = clamp(percentage, -1, 1)
		brightness = hsv[2] + percent
		brightness = clamp(brightness, 0, 1)
		newrgb = colorsys.hsv_to_rgb(hsv[0], hsv[1], brightness)
		return RgbColor(tuple(255*x for x in newrgb))

	def setBrightness(self, percent: float):
		rgb = self.asPercents()
		hsv = colorsys.rgb_to_hsv(rgb[0], rgb[1], rgb[2])
		value = clamp(percent, 0, 1)
		newrgb = colorsys.hsv_to_rgb(hsv[0], hsv[1], value)
		return RgbColor(tuple(255*x for x in newrgb))
