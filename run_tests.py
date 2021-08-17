import sys
from src.test.framework.test_runner import TestRunner, TestRunnerConfig

if __name__ == "__main__":
	config: TestRunnerConfig = TestRunnerConfig(
		fileGlob = "src/test/**/*_test.py",
		verbosity="SUMMARY"
	)
	result = TestRunner(config).run()
	sys.exit(0 if result else 1)
