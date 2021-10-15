import sys
from assert4py.test_runner import TestRunner, TestRunnerConfig

if __name__ == "__main__":
	config: TestRunnerConfig = TestRunnerConfig(
		fileGlob = "tests/**/*_test.py",
		verbosity="INFO" # SUMMARY, INFO, VERBOSE
	)
	result = TestRunner(config).run()
	sys.exit(0 if result else 1)
