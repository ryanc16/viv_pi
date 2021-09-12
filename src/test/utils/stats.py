from src.test.framework.annotations import focus, test
from src.test.framework.assertions import assertThat
from src.main.utils.stats import Stats, within_weighted_std, within_std

@test
class StatsTest:

  @test
  def testWithinStd():
    input = [80.5, 80.0, 79.5]
    std_factor = 7
    value1 = 82
    result1 = within_std(input, value1, std_factor)
    assertThat(result1).isTrue()
    value2 = 65
    result2 = within_std(input, value2, std_factor)
    assertThat(result2).isFalse()

  @test
  def testAdjustedMean():
    values = [1, 2, 3, 4, 5, 8, 8, 8, 8, 8]
    mean = Stats.mean(values)
    input = 7.0
    expected = Stats.mean([mean, input])
    result = Stats.adjusted_mean(values, input)
    assertThat(result).isEqualTo(expected)

  @test
  def testAdjustedWeightedMean():
    values = [1, 2, 3, 4, 5, 8, 8, 8, 8, 8]
    input = 9
    result = Stats.adjusted_weighted_mean(values, input)
    assertThat(result).isCloseTo(7.181818, 1e-6)

  @test
  def testWeightedAverage():
    values = [1, 2, 3, 4, 5, 8, 8, 8, 8, 9]
    print(Stats.mean(values))
    result = Stats.weighted_average(values)
    assertThat(result).isCloseTo(7, 1e-1)