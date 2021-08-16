from src.test.framework.assertions import assertThat
from typing import Tuple

def colorTupleComparator(actual: Tuple, expected: Tuple):
  assertThat(actual).hasLengthOf(3)
  assertThat(expected).hasLengthOf(3)
  for i in range(3):
    assertThat(actual[i]).isCloseTo(expected[i], 1e-9)
  return True