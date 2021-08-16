

from src.main.utils.colors import Colors
from src.main.utils.color_functions import ColorFunctions


class NaturalColors:
  DAWN = ColorFunctions.blend_colors(Colors.GRAY, Colors.CYAN, 0.25).brightness(0.05)
  MIDDAY = ColorFunctions.blend_colors(Colors.WHITE, Colors.YELLOW, 0.7)
  EARLY_EVENING = Colors.YELLOW.lighten(0.05).adjust_brightness(+0.1)
  LATE_EVENING = Colors.ORANGE.lighten(0.05).brightness(0.25)
  EVENING = ColorFunctions.blend_colors(EARLY_EVENING, LATE_EVENING, 0.5)
  DUSK = ColorFunctions.blend_colors(Colors.ORANGE.lighten(0.05), Colors.BLUE.lightness(0.3), 0.5).brightness(0.15)
  NIGHT = Colors.BLUE.lightness(0.55).brightness(0.005)