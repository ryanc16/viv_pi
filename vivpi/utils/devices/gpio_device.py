
from typing import Tuple

from dataclasses import dataclass

@dataclass
class GpioDevice:
  pins: Tuple[int]