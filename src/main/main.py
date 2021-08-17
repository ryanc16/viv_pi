from datetime import datetime
from time import sleep

from src.main.system_config import SystemConfig
from src.main.controllers.lighting.lighting_controller import LightingController

class Main:

	def __init__(self, systemConfig: SystemConfig):
		print("viv-pi started at", datetime.now())
		self.systemConfig = systemConfig

		if systemConfig.lighting.ENABLED:
			print("starting: LightingController")
			self.lightingController = LightingController(systemConfig.lighting)
			self.lightingController.start()
		
		while True:
			self.onUpdate()
			sleep(1)

	def onUpdate(self):
		pass
