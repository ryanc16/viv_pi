import traceback

class Test:

	tests = {}
	
	def __init__(self):
		print(f"Starting: {self.__class__.__name__}")
		self.total = len(Test.tests[self.__module__].keys())
		self.success = 0
		self.fail = 0
		self.skipped = 0
		percent = lambda x: "{:3.2f}".format(x*100)+"%"
		for test in Test.tests[self.__module__]:
			test_name = test.__name__
			print(f"  {test_name}", end="\r")
			if Test.tests[self.__module__][test]['skip'] == True:
				self.skipped+=1
				print(f"  {test_name}", "SKIP")
				continue
			try:
				test()
				self.success+=1
				print(f"  {test_name}", "PASS")
			except AssertionError as reason:
				self.fail+=1
				print(f"  {test_name}", "FAIL")
				traceback.print_exception(reason, reason, reason.__traceback__)
		print(f"{self.total} Total, {self.success} Pass, {self.fail} Fail, {self.skipped} Skipped. ({percent(self.success/(self.total-self.skipped))})\n")