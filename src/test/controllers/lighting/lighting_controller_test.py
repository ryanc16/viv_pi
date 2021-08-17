from src.main.controllers.lighting.lighting_config import LightingConfig
from src.main.controllers.lighting.lighting_controller import LightingController
from src.main.controllers.lighting.natural_colors import NaturalColors
from src.main.utils.time_functions import TimeFunctions
from src.test.comparators.color_comparator import rgbColorComparator
from src.test.framework.annotations import beforeEach, test
from src.test.framework.assertions import assertThat

lightingConfig = LightingConfig(
  GPIO=None,
  ENABLED=False,
  DEMO=False,
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

@test
class LightingControllerTest:

  @beforeEach
  def setUp(ctx):
    ctx.lightingController = LightingController(lightingConfig)

  @test
  def testInitialization(ctx):
    assertThat(ctx.lightingController.lightingConfig).isEqualTo(lightingConfig)
    assertThat(ctx.lightingController.start_time).isEqualTo(lightingConfig.START_TIME)
    assertThat(ctx.lightingController.duration).isEqualTo(lightingConfig.DURATION)
    assertThat(ctx.lightingController.min_brightness).isEqualTo(lightingConfig.MIN_BRIGHTNESS)
    assertThat(ctx.lightingController.max_brightness).isEqualTo(lightingConfig.MAX_BRIGHTNESS)
    assertThat(ctx.lightingController.color_steps).isTypeOf(list)
    assertThat(ctx.lightingController.enabled).isFalse()

  @test
  def testGenerateColorSteps(ctx):
    color_steps = ctx.lightingController.generateColorSteps()
    expected_length = lightingConfig.DURATION * 60
    assertThat(color_steps).hasLengthOf(expected_length)

  @test
  def testGetColorForTime(ctx):
    start_time = TimeFunctions.timeFromHours(lightingConfig.START_TIME)
    start_color = ctx.lightingController.getColorForTime(start_time)
    expected_start_color = lightingConfig.COLORS[0]
    assertThat(start_color).whenComparedUsing(rgbColorComparator).isEqualTo(expected_start_color)

    end_time = TimeFunctions.timeFromHours(lightingConfig.START_TIME+lightingConfig.DURATION)
    end_color = ctx.lightingController.getColorForTime(end_time)
    expected_end_color = lightingConfig.COLORS[len(lightingConfig.COLORS)-1]
    assertThat(end_color).whenComparedUsing(rgbColorComparator).isEqualTo(expected_end_color)

  @test
  def testGetBrightnessForTime(ctx):
    time = TimeFunctions.timeFromHours(lightingConfig.START_TIME)
    brightness = ctx.lightingController.getBrightnessForTime(time)
    assertThat(brightness).isCloseTo(0, 1e-9)
