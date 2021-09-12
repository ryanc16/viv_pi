from dataclasses import dataclass
from typing import List
from src.main.utils.devices.rgb_gpio_device import RgbGpioDevice
from src.main.utils.rgb_color import RgbColor

@dataclass
class LightingConfig:
	ENABLED: bool
	DEMO: bool
	GPIO: RgbGpioDevice
	START_TIME: float
	DURATION: float
	MIN_BRIGHTNESS: float
	MAX_BRIGHTNESS: float
	COLORS: List[RgbColor]