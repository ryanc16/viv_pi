
from src.test.framework.test_runner import TestRunner
from src.test.utils.time_functions_test import TimeFunctionsTest
from src.test.utils.color_functions_test import ColorFunctionsTest
from src.test.utils.rgb_color_test import RgbColorTest
from src.test.utils.colors_test import ColorsTest

if __name__ == "__main__":
	tests = [
		TimeFunctionsTest,
		ColorFunctionsTest,
		RgbColorTest,
		ColorsTest
	]
	TestRunner(tests).run()
