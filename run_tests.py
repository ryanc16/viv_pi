
from src.test.framework.test_runner import TestRunner
from src.test.utils.time_functions_test import TimeFunctionsTest

if __name__ == "__main__":
	tests = [
		TimeFunctionsTest
	]
	TestRunner(tests).run()
