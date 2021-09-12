from dataclasses import dataclass
from src.main.utils.devices.temp_hum_gpio_device import TempHumGpioDevice


@dataclass
class TemperatureConfig:
  ENABLED: bool
  DEMO: bool
  GPIO: TempHumGpioDevice
  SCALE: str
  MAX_TEMPERATURE: float
  MIN_TEMPERATURE: float