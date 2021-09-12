from src.main.utils.color_functions import ColorFunctions
from src.main.controllers.lighting.lighting_config import LightingConfig
from src.main.controllers.lighting.lighting_controller import LightingController
from src.main.controllers.lighting.natural_colors import NaturalColors
from src.main.utils.colors import Colors
from src.main.utils.time_functions import TimeFunctions
from src.test.comparators.color_comparator import rgbColorComparator
from src.test.framework.annotations import beforeEach, focus, test
from src.test.framework.assertions import assertThat
from src.test.framework.mocks import Mock, assertMock, mock, mockMethod

lightingConfig = LightingConfig(
  ENABLED=False,
  DEMO=False,
  GPIO=None,
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
    ctx.ColorFunctionsMock = mock(ColorFunctions)
    ctx.ColorFunctionsMock.interpolateRgbGradient.thenReturn([NaturalColors.DAWN, NaturalColors.NIGHT])
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
    ctx.ColorFunctionsMock.reset()
    ctx.lightingController.generateColorSteps()
    expected_length = lightingConfig.DURATION * 60
    assertMock(ctx.ColorFunctionsMock.interpolateRgbGradient).toHaveBeenCalledTimes(1)
    assertMock(ctx.ColorFunctionsMock.interpolateRgbGradient).toHaveBeenCalledWith((lightingConfig.COLORS, expected_length))

  @test
  def testGetColorForTime(ctx):
    timeFnMock = mockMethod(TimeFunctions, 'isTimeWithinRange')
    timeFnMock.thenReturn(True)

    start_time = TimeFunctions.timeFromHours(lightingConfig.START_TIME)
    start_color = ctx.lightingController.getColorForTime(start_time)
    expected_start_color = lightingConfig.COLORS[0]
    assertThat(start_color).whenComparedUsing(rgbColorComparator).isEqualTo(expected_start_color)
    assertMock(timeFnMock).toHaveBeenCalledTimes(1)
    assertMock(timeFnMock).toHaveLastBeenCalledWith((start_time, lightingConfig.START_TIME, lightingConfig.START_TIME + lightingConfig.DURATION))

    end_time = TimeFunctions.timeFromHours(lightingConfig.START_TIME + lightingConfig.DURATION)
    end_color = ctx.lightingController.getColorForTime(end_time)
    expected_end_color = lightingConfig.COLORS[len(lightingConfig.COLORS)-1]
    assertThat(end_color).whenComparedUsing(rgbColorComparator).isEqualTo(expected_end_color)
    assertMock(timeFnMock).toHaveBeenCalledTimes(2)
    assertMock(timeFnMock).toHaveLastBeenCalledWith((end_time, lightingConfig.START_TIME, lightingConfig.START_TIME + lightingConfig.DURATION))

  @test
  def testGetColorForTimeOutsideRange(ctx):
    timeFnMock = mockMethod(TimeFunctions, 'isTimeWithinRange')
    timeFnMock.thenReturn(False)
    expected_color = Colors.BLACK

    time1 = TimeFunctions.timeFromHours(0)
    color1 = ctx.lightingController.getColorForTime(time1)
    assertThat(color1).whenComparedUsing(rgbColorComparator).isEqualTo(expected_color)
    assertMock(timeFnMock).toHaveLastBeenCalledWith((time1, lightingConfig.START_TIME, lightingConfig.START_TIME + lightingConfig.DURATION))

    time2 = TimeFunctions.timeFromHours(3)
    color2 = ctx.lightingController.getColorForTime(time2)
    assertThat(color2).whenComparedUsing(rgbColorComparator).isEqualTo(expected_color)
    assertMock(timeFnMock).toHaveLastBeenCalledWith((time2, lightingConfig.START_TIME, lightingConfig.START_TIME + lightingConfig.DURATION))

    time3 = TimeFunctions.timeFromHours(21)
    color3 = ctx.lightingController.getColorForTime(time3)
    assertThat(color3).whenComparedUsing(rgbColorComparator).isEqualTo(expected_color)
    assertMock(timeFnMock).toHaveLastBeenCalledWith((time3, lightingConfig.START_TIME, lightingConfig.START_TIME + lightingConfig.DURATION))

    time4 = TimeFunctions.timeFromHours(24)
    color4 = ctx.lightingController.getColorForTime(time4)
    assertThat(color4).whenComparedUsing(rgbColorComparator).isEqualTo(expected_color)
    assertMock(timeFnMock).toHaveLastBeenCalledWith((time4, lightingConfig.START_TIME, lightingConfig.START_TIME + lightingConfig.DURATION))

    assertMock(timeFnMock).toHaveBeenCalledTimes(4)

  @test
  def testGetBrightnessForTime(ctx):
    time = TimeFunctions.timeFromHours(lightingConfig.START_TIME)
    brightness = ctx.lightingController.getBrightnessForTime(time)
    assertThat(brightness).isCloseTo(0, 1e-9)
