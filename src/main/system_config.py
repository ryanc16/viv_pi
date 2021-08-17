from dataclasses import dataclass

from src.main.controllers.lighting.lighting_config import LightingConfig

@dataclass
class SystemConfig:
	lighting: LightingConfig