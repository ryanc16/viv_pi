from datetime import datetime
import threading
from typing import List

from vivpi.controllers.controller import Controller
from vivpi.system_config import ControllerConfig, SystemConfig
from vivpi.services.input_reporting_service import InputReportingService

class Main:

  def __init__(self, systemConfig: SystemConfig):
    self.systemConfig = systemConfig
    self.controllers: List[Controller] = []

  def onStart(self):
    print("viv-pi started at", datetime.now())
    for ctrlConfig in self.systemConfig.controllers:
      self._startController(ctrlConfig)
    
    self.exit = threading.Event()
    while not self.exit.is_set():
      self.onUpdate()
      self.exit.wait(1)

  def onStop(self):
    self.exit.set()
    for controller in self.controllers:
      print(f"Stopping: {controller.__class__.__name__}")
      controller.stop()
    print("viv-pi stopped at", datetime.now())

  def onUpdate(self):
    ids = ["temp", "hum"]
    values = InputReportingService.instance().checkAll(ids)
    out = []
    for i in range(len(values)):
      out.append(f"{ids[i]}: {values[i]}")
    print(str.join(", ", out), end="\r")

  def _startController(self, ctrlConfig: ControllerConfig):
    if ctrlConfig.config.ENABLED:
      print(f"Starting: {ctrlConfig.type.__name__}")
      controller: Controller = ctrlConfig.type(ctrlConfig.config)
      controller.start()
      self.controllers.append(controller)
