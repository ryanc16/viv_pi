import glob
import importlib
import inspect
import os
import traceback
from dataclasses import dataclass
from datetime import datetime
from types import FunctionType
from functools import reduce

from src.test.framework.test_context import TestContext


@dataclass
class TestRunnerConfig:
	fileGlob: str
	verbosity: str
class TestRunner:
	scanned = {}
	tests = {}
	def __init__(self, config: TestRunnerConfig):
		self.config = config
		self._scanTests()
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
		print("Starting tests")
		if self.config.verbosity != "SUMMARY":
			print("")
		start = datetime.now()
		for suite in self.tests:
			results = self.runSuite(suite)
			self.total += results[0]
			self.success += results[1]
			self.fail += results[2]
			self.skipped += results[3]
		stop = datetime.now()
		if self.config.verbosity != "VERBOSE":
			print("")
		print("Tests complete")
		print(f"{self.total} Total, {self.success} Pass, {self.fail} Fail, {self.skipped} Skipped. ({percent(self.success/((self.total-self.skipped)+1e-9))})")
		print(f"Took {stop-start}")
		return self.fail == 0

	def runSuite(self, suite):
		if self.config.verbosity != "SUMMARY":
			print(f"Starting: {suite.__name__}")
		suite_meta = TestRunner.tests[suite]
		tests = suite_meta['tests']
		total = len(tests.keys())
		success = 0
		fail = 0
		skipped = 0
		percent = lambda x: "{:3.2f}".format(x*100)+"%"
		ctx = TestContext()
		if suite_meta['beforeAll'] is not None:
			suite_meta['beforeAll'](ctx)
		for test in tests.keys():
			if suite_meta['beforeEach'] is not None:
				suite_meta['beforeEach'](ctx)
			result = self.runOne(suite, test, ctx)
			if result == True:
				success+=1
			elif result == None:
				skipped+=1
			else:
				fail+=1
		if self.config.verbosity != "SUMMARY":
			print(f"{total} Total, {success} Pass, {fail} Fail, {skipped} Skipped. ({percent(success/((total-skipped)+1e-9))})")
		if self.config.verbosity == "VERBOSE":
			print("")
		return (total, success, fail, skipped)
	
	def runOne(self, suite, test: FunctionType, ctx: TestContext) -> bool:
		test_name = test.__name__
		if self.config.verbosity == "VERBOSE":
			print(f"  {test_name}", end="\r")
		if TestRunner.tests[suite]['tests'][test]['skip'] == True:
			if self.config.verbosity == "VERBOSE":
				print(f"  {test_name}", "SKIP")
			return None
		try:
			if 'ctx' in inspect.getargspec(test).args:
				pre_ctx = ctx.__dict__.copy()
				test(ctx)
				if ctx.__dict__.keys() != pre_ctx.keys():
					raise Exception('Do add or remove items from test context within a test method')
			else:
				test()
			if self.config.verbosity == "VERBOSE":
				print(f"  {test_name}", "PASS")
			return True
		except Exception as reason:
			if self.config.verbosity == "VERBOSE":			
				print(f"  {test_name}", "FAIL")
			traceback.print_exception(reason, reason, reason.__traceback__)
			return False

	def _scanTests(self):
		if self.config.verbosity == "VERBOSE":
			print("Scanning for tests")
		files = []
		if self.config is not None:
			files = glob.glob(self.config.fileGlob, recursive=True)
		else:
			files = glob.glob("src/test/**/*_test.py", recursive=True)
		if self.config.verbosity == "VERBOSE":
			print(f"Found {len(files)} test files")
		for file_path in files:
			mod_path = file_path.replace(os.path.sep, '/').replace('/', '.').replace('.py', '')
			importlib.import_module(mod_path)
			# The annotations take care of the rest
		if self.config.verbosity == "VERBOSE":
			suites = len(TestRunner.scanned.keys())
			tests = reduce(
				lambda a,b: a+b,
				list(
					map(
						lambda suite: len(TestRunner.scanned[suite]['tests'].keys()),
						TestRunner.scanned.keys()
					)
				)
			)
			print(f"Loaded {suites} test suites with {tests} tests")
