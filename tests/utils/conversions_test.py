from assert4py.annotations import focus, test
from assert4py.assertions import assertThat
from vivpi.utils.conversions import Conversions

@test
class ConversionsTest:

  @test
  def testCtoF():
    input = 25.0
    expected = 77.0
    result = Conversions.CtoF(input)
    assertThat(result).isEqualTo(expected)

  @test
  def testFtoC():
    input = 77.0
    expected = 25.0
    result = Conversions.FtoC(input)
    assertThat(result).isEqualTo(expected)