from typing import Dict
from vivpi.controllers.audio.audio_config import AudioConfig
from vivpi.controllers.audio.audio_controller import AudioController
from vivpi.controllers.lighting.lighting_controller import LightingController
from vivpi.controllers.temperature.temperature_controller import TemperatureController
from vivpi.controllers.humidity.humidity_controller import HumidityController
from vivpi.controllers.humidity.humidity_config import HumidityConfig
from vivpi.controllers.temperature.temperature_config import TemperatureConfig
from vivpi.utils.devices.gpio_device import GpioDevice
from vivpi.utils.devices.rgb_gpio_device import RgbGpioDevice
from vivpi.utils.devices.temp_hum_gpio_device import TempHumGpioDevice
from vivpi.system_config import ControllerConfig, SystemConfig
from vivpi.controllers.lighting.lighting_config import LightingConfig
from vivpi.controllers.lighting.natural_colors import NaturalColors


GPIO: Dict[str, GpioDevice] = {
  'rgb': RgbGpioDevice(r=26, g=19, b=13),
  'temp/hum': TempHumGpioDevice(12)
}

SYSTEM_CONFIG: SystemConfig = SystemConfig(
  controllers = [
    ControllerConfig(
      type = LightingController,
      config = LightingConfig(
        ENABLED=True,
        DEMO=False,
        GPIO=GPIO['rgb'],
        START_TIME=6,
        DURATION=14,
        MIN_BRIGHTNESS=0,
        MAX_BRIGHTNESS=1,
        COLORS=[
          NaturalColors.DAWN,     # 06:00
          NaturalColors.MIDDAY,   # 07:45
          NaturalColors.MIDDAY,   # 09:30
          NaturalColors.MIDDAY,   # 11:15
          NaturalColors.MIDDAY,   # 13:00
          NaturalColors.EVENING,  # 14:45
          NaturalColors.DUSK,     # 16:30
          NaturalColors.NIGHT     # 18:15
        ]
      )
    ),
    ControllerConfig(
      type = TemperatureController,
      config = TemperatureConfig(
        ENABLED=True,
        DEMO=False,
        GPIO=GPIO['temp/hum'],
        SCALE="F",
        MIN_TEMPERATURE=75,
        MAX_TEMPERATURE=90
      )
    ),
    ControllerConfig(
      type = HumidityController,
      config = HumidityConfig(
        ENABLED=True,
        DEMO=False,
        GPIO=GPIO['temp/hum'],
        MIN_HUMIDITY=40,
        MAX_HUMIDITY=70
      )
    ),
    ControllerConfig(
      type=AudioController,
      config=AudioConfig(
        ENABLED=True,
        DEMO=True,
        VOLUME=80,
        MEDIA="~/media/"
      )
    )
  ]
)
