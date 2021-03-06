from vivpi.controllers.controller import Controller
from vivpi.controllers.humidity.humidity_config import HumidityConfig
from vivpi.services.input_reporting_service import InputReportingService
import threading


class HumidityController(Controller):
  
  def __init__(self, humidityConfig: HumidityConfig):
    self.humidityConfig = humidityConfig
    self.sensor = self.humidityConfig.GPIO
    self.enabled = False

  def start(self):
    self.enabled = True
    self.exit = threading.Event()
    if self.humidityConfig.DEMO == True:
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
      if self.sensor.humidity is not None:
        InputReportingService.instance().report("hum", f"{round(self.sensor.humidity, 1)} %")
      self.exit.wait(5)
    self.sensor.stop()

  def demo(self):
    pass
