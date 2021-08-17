from dataclasses import dataclass
from typing import List
from src.main.utils.rgb_color import RgbColor

@dataclass
class LightingGPIOConfig:
	R: int
	G: int
	B: int

@dataclass
class LightingConfig:
	ENABLED: bool
	DEMO: bool
	GPIO: LightingGPIOConfig
	START_TIME: float
	DURATION: float
	MIN_BRIGHTNESS: float
	MAX_BRIGHTNESS: float
	COLORS: List[RgbColor]