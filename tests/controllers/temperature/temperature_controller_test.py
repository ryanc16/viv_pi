from assert4py.annotations import beforeEach, focus, test, skip
from assert4py.assertions import assertThat
from vivpi.utils.conversions import Conversions

@test
@skip
class TemperatureControllerTest:

  @beforeEach
  def setUp(ctx):
    from vivpi.controllers.temperature.temperature_controller import TemperatureController
    from vivpi.controllers.temperature.temperature_config import TemperatureConfig

    ctx.temperatureConfig = TemperatureConfig(
      ENABLED=False,
      DEMO=False,
      GPIO=None,
      MIN_TEMPERATURE=75,
      MAX_TEMPERATURE=92,
      SCALE="F"
    )
    ctx.temperatureController = TemperatureController(ctx.temperatureConfig)

  @test
  def testRecordTempReadingEmptyArray(ctx):
    ctx.temperatureController.temp_readings = []
    input = 25.0
    expected = [Conversions.CtoF(input)]
    ctx.temperatureController.recordTempReading(input)
    assertThat(ctx.temperatureController.temp_readings).isEqualTo(expected)

  @test
  def testRecordTempReadings1Reading(ctx):
    ctx.temperatureController.temp_readings = [76.0]
    input = 25.0
    expected = [76.0, 76.5]
    ctx.temperatureController.recordTempReading(input)
    assertThat(ctx.temperatureController.temp_readings).isEqualTo(expected)

  @test
  def testRecordTempReadings10Readings(ctx):
    ctx.temperatureController.temp_readings = [76.0, 76.25, 76.0, 76.25, 76.0, 75.75, 76.0, 75.75, 75.75, 76.0]
    input = 25.0
    expected = [76.25, 76.0, 76.25, 76.0, 75.75, 76.0, 75.75, 75.75, 76.0, 76.75]
    ctx.temperatureController.recordTempReading(input)
    assertThat(ctx.temperatureController.temp_readings).isEqualTo(expected)
