from dataclasses import dataclass

from src.main.utils.devices.temp_hum_gpio_device import TempHumGpioDevice


@dataclass
class HumidityConfig:
  ENABLED: bool
  DEMO: bool
  GPIO: TempHumGpioDevice
  MAX_HUMIDITY: float
  MIN_HUMIDITY: float