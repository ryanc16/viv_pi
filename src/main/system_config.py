from dataclasses import dataclass
from typing import Dict, List
from src.main.controllers.controller import Controller


@dataclass
class ControllerConfig:
	type: Controller
	config: object
@dataclass
class SystemConfig:
	controllers: List[ControllerConfig]