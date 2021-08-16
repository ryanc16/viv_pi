
from src.test.framework.test_runner import TestRunner
from src.test.utils.time_functions_test import TimeFunctionsTest
from src.test.utils.color_functions_test import ColorFunctionsTest

if __name__ == "__main__":
	tests = [
		TimeFunctionsTest,
		ColorFunctionsTest
	]
	TestRunner(tests).run()
