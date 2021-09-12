from typing import List
import threading

from src.main.utils.devices.dht11 import DHT11Result
from src.main.utils.devices.gpio_device import GpioDevice
from src.main.utils.stats import Stats, within_weighted_std
from src.main.utils.data import Data

class TempHumGpioDevice(GpioDevice):

  def __init__(self, pin):
    super().__init__(pins=(pin))
    self.enabled = False
    self.sensor = None
    self.temp_readings = []
    self.hum_readings = []
    self.window = 10
    self.err_count = 0
    self.polling = 1
    self.temperature = None
    self.humidity = None
    self.thread = None
    from src.main.utils.devices.dht11 import DHT11
    self.sensor = DHT11(self.pins)

  def start(self):
    if self.enabled == False:
      self.enabled = True
      self.exit = threading.Event()
      self.thread = threading.Thread(target=self.poll)
      self.thread.start()
  
  def stop(self):
    self.enabled = False
    self.exit.set()

  def poll(self):
    while not self.exit.is_set():
      result = self.sensor.read()
      if result.is_valid():
        self.err_count = 0
        self.onValidReading(result)
      else:
        self.err_count+=1
        self.onErrorReading()
      self.exit.wait(self.polling)

  def onValidReading(self, reading: DHT11Result):
    self.recordTempReading(reading.temperature)
    self.recordHumReading(reading.humidity)
    if len(self.temp_readings) > 0:
      self.temperature = self.temp_readings[-1]
      self.humidity = self.hum_readings[-1]

  def recordTempReading(self, temp_reading: float):
    self._filterReadingLogic(temp_reading, self.temp_readings)

  def recordHumReading(self, hum_reading):
    self._filterReadingLogic(hum_reading, self.hum_readings)

  def _filterReadingLogic(self, reading: float, history: List[float]):
    add = False
    if len(history) > self.window:
      if within_weighted_std(history, reading, 3):
        add = True
      else:
        add = False
    else:
      add = True

    if add:
      if len(history) > 0:
        reading = Stats.adjusted_weighted_mean(history, reading)
      reading = Data.round_tenths(reading)
      history.append(reading)

    if len(history) > self.window:
      history.pop(0)

  def onErrorReading(self):
    if self.err_count % 5 == 0:
      if len(self.temp_readings) > 0:
        self.temp_readings.pop(0)
      if len(self.hum_readings) > 0:
        self.hum_readings.pop(0)
