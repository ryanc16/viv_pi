from datetime import datetime
from typing import List

from src.test.framework.test import Test

class TestRunner:

	def __init__(self, tests: List[Test]):
		self._tests = tests
		self.total = 0
		self.success = 0
		self.fail = 0
		self.skipped = 0

	def run(self):
		self.total = 0
		self.success = 0
		self.fail = 0
		self.skipped = 0
		percent = lambda x: "{:3.2f}".format(x*100)+"%"
		print("Starting tests...\n")
		start = datetime.now()
		for _test in self._tests:
			test: Test = _test()
			self.total += test.total
			self.success += test.success
			self.fail += test.fail
			self.skipped += test.skipped
		stop = datetime.now()
		print("Tests complete\n")
		print(f"{self.total} Total, {self.success} Pass, {self.fail} Fail, {self.skipped} Skipped. ({percent(self.success/(self.total-self.skipped))})\n")
		print(f"Took {stop-start}")