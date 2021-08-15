import math
from typing import List
from src.main.utils.rgb_color import RgbColor

class ColorFunctions:

	def blend_colors(start_colour: RgbColor, end_colour: RgbColor, blend_percentage: float) -> RgbColor:
		start_colour = start_colour.as_rgb()
		end_colour = end_colour.as_rgb()
		blended_color = [0, 0, 0]
		for i in range(len(blended_color)):
			diff = end_colour[i] - start_colour[i]
			if diff != 0:
				blend_shift = (diff * blend_percentage)
				blended_color[i] = start_colour[i] + blend_shift
			else:
				blended_color[i] = start_colour[i]
		return RgbColor(blended_color[0], blended_color[1], blended_color[2])

	def interpolate_rgb(startcolor: RgbColor, goalcolor: RgbColor, steps: int) -> List[RgbColor]:
		"""
		Take two RGB color sets and mix them over a specified number of steps.  Return the list
		"""
		startcolor = startcolor.as_rgb()
		goalcolor = goalcolor.as_rgb()
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

		FracR = DiffR/steps
		FracG = DiffG/steps
		FracB = DiffB/steps

		buffer = []

		for i in range(steps+1):
			iR = (R + (FracR * i))
			iG = (G + (FracG * i))
			iB = (B + (FracB * i))

			color = RgbColor(iR, iG, iB)
			buffer.append(color)

		return buffer

	def interpolate_rgb_gradient(colors: List[RgbColor], steps: int) -> List[RgbColor]:
		color_steps = []
		repeat = len(colors)-1
		for i in range(0, repeat):
			color_steps += ColorFunctions.interpolate_rgb(colors[i], colors[i+1], math.floor(steps/repeat))
		return color_steps