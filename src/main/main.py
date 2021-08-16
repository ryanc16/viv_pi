from datetime import datetime
from time import sleep

from src.main.config import SystemConfig
from src.main.controllers.lighting.lighting_controller import LightingController

config: SystemConfig = SystemConfig
class Main:

	def __init__(self):
		print("viv-pi started at", datetime.now())
		if config.lighting.ENABLED:
			self.lightingController = LightingController()
			self.lightingController.start()

	def onUpdate(self):
		while True:
			sleep(1)

Main().onUpdate()