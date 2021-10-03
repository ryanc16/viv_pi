from assert4py.annotations import focus, test
from assert4py.assertions import assertThat
from vivpi.utils.data import Data

@test
class DataTest:

  @test
  def testRoundHalves():
    input1 = 100.24
    expected1 = 100
    result1 = Data.round_halves(input1)
    assertThat(result1).isEqualTo(expected1)

    input2 = 67.6
    expected2 = 67.5
    result2 = Data.round_halves(input2)
    assertThat(result2).isEqualTo(expected2)

  @test
  def testRoundThirds():
    input1 = 100.24
    expected1 = 100.33
    result1 = Data.round_thirds(input1)
    assertThat(result1).isCloseTo(expected1, 1e-2)

    input2 = 100.75
    expected2 = 100.66
    result2 = Data.round_thirds(input2)
    assertThat(result2).isCloseTo(expected2, 1e-2)

  @test
  def testRoundQuarters():
    input1 = 76.7
    expected1 = 76.75
    result1 = Data.round_quarters(input1)
    assertThat(result1).isEqualTo(expected1)
    
    input2 = 76.31
    expected2 = 76.25
    result2 = Data.round_quarters(input2)
    assertThat(result2).isEqualTo(expected2)

  @test
  def testRoundTenths():
    input1 = 76.1234
    expected1 = 76.1
    result1 = Data.round_tenths(input1)
    assertThat(result1).isEqualTo(expected1)

    input2 = 76.4567
    expected2 = 76.5
    result2 = Data.round_tenths(input2)
    assertThat(result2).isEqualTo(expected2)