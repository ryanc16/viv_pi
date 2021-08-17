

from src.main.utils.colors import Colors
from src.main.utils.color_functions import ColorFunctions


class NaturalColors:
  DAWN = ColorFunctions.blendColors(Colors.GRAY, Colors.CYAN, 0.25).setBrightness(0.05)
  MIDDAY = ColorFunctions.blendColors(Colors.WHITE, Colors.YELLOW, 0.7)
  EARLY_EVENING = Colors.YELLOW.lighten(0.05).adjust_brightness(+0.1)
  LATE_EVENING = Colors.ORANGE.lighten(0.05).setBrightness(0.25)
  EVENING = ColorFunctions.blendColors(EARLY_EVENING, LATE_EVENING, 0.5)
  DUSK = ColorFunctions.blendColors(Colors.ORANGE.lighten(0.05), Colors.BLUE.lightness(0.3), 0.5).setBrightness(0.15)
  NIGHT = Colors.BLUE.lightness(0.55).setBrightness(0.005)