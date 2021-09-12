from src.main.controllers.controller import Controller
from src.main.utils.conversions import Conversions
from src.main.controllers.temperature.temperature_config import TemperatureConfig
from src.main.services.input_reporting_service import InputReportingService
import threading


class TemperatureController(Controller):
  
  def __init__(self, temperatureConfig: TemperatureConfig):
    self.temperatureConfig = temperatureConfig
    self.sensor = self.temperatureConfig.GPIO
    self.enabled = False

  def start(self):
    self.enabled = True
    self.exit = threading.Event()
    if self.temperatureConfig.DEMO == True:
      self.thread = threading.Thread(target=self.demo)
    else:
      self.thread = threading.Thread(target=self.realtime)
    self.thread.start()

  def stop(self):
    self.enabled = False
    self.exit.set()

  def realtime(self):
    self.sensor.start()
    while not self.exit.is_set():
      if self.sensor.temperature is not None:
        if self.temperatureConfig.SCALE == "F":
          InputReportingService.instance().report("temp", f"{round(Conversions.CtoF(self.sensor.temperature), 1)} F")
        else:
          InputReportingService.instance().report("temp", f"{self.sensor.temperature} C")
      self.exit.wait(5)
    self.sensor.stop()

  def demo(self):
    pass
