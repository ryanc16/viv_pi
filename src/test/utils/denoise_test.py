from src.test.framework.annotations import focus, test
from src.test.framework.assertions import assertThat
from src.main.utils.denoise import eliminateNoise

@test
class DenoiseTest:

  @test
  def testDenoiseValuesSize1():
    input = [80.42]
    expected = [80.42]
    result = eliminateNoise(input)
    assertThat(result).isEqualTo(expected)

  @test
  def testDenoiseValuesSize10():
    input =    [80, 82, 81.5, 81.5, 81.5, 81.5, 81, 80.5, 80.5, 65]
    expected = [80, 82, 81.5, 81.5, 81.5, 81.5, 81, 80.5, 80.5]
    result = eliminateNoise(input)
    assertThat(result).isEqualTo(expected)
