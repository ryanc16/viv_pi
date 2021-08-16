from dataclasses import dataclass

from src.main.controllers.lighting.lighting_config import LightingConfig, LightingGPIOConfig
from src.main.controllers.lighting.natural_colors import NaturalColors


@dataclass
class Config:
	lighting: LightingConfig

SystemConfig: Config = Config(
	lighting = LightingConfig(
		ENABLED=True,
		GPIO=LightingGPIOConfig(
			R = 26,
			G = 19,
			B = 13
		),
		START_TIME=6,
		DURATION=14,
		MIN_BRIGHTNESS=0,
		MAX_BRIGHTNESS=1,
		COLORS=[
			NaturalColors.DAWN,			# 06:00
			NaturalColors.MIDDAY,		# 07:45
			NaturalColors.MIDDAY,		# 09:30
			NaturalColors.MIDDAY,		# 11:15
			NaturalColors.MIDDAY,		# 13:00
			NaturalColors.EVENING,	# 14:45
			NaturalColors.DUSK,			# 16:30
			NaturalColors.NIGHT			# 18:15
		]
	)
)
