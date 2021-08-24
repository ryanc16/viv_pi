from typing import Tuple

from src.main.utils.rgb_color import RgbColor
from src.test.framework.assertions import assertThat


def colorTupleComparator(actual: Tuple, expected: Tuple) -> bool:
  assertThat(actual).hasLengthOf(3)
  assertThat(expected).hasLengthOf(3)
  for i in range(3):
    assertThat(actual[i]).isCloseTo(expected[i], 1e-9)
  return True

def rgbColorComparator(actual: RgbColor, expected: RgbColor) -> bool:
  return colorTupleComparator(actual.asRgb(), expected.asRgb())
