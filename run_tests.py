
from src.test.framework.test_runner import TestRunner
from src.test.utils.time_functions_test import TimeFunctionsTest
from src.test.utils.color_functions_test import ColorFunctionsTest
from src.test.utils.rgb_color_test import RgbColorTest

if __name__ == "__main__":
	tests = [
		TimeFunctionsTest,
		ColorFunctionsTest,
		RgbColorTest
	]
	TestRunner(tests).run()
