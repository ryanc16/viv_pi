from src.test.framework.annotations import focus, test
from src.test.framework.assertions import assertThat
from src.main.utils.conversions import Conversions

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