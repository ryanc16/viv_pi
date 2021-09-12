from src.main.utils.devices.gpio_device import GpioDevice

class RgbGpioDevice(GpioDevice):
  def __init__(self, r: int, g: int, b: int):
    super().__init__(pins=(r, g, b))
