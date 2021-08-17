import inspect
from types import FunctionType

from src.test.framework.test_runner import TestRunner


def initializeTestModule(module: str):
	TestRunner.scanned[module] = {
		'beforeAll': None,
		'beforeEach': None,
		'tests': {}
	}

def test(methodOrClass: FunctionType):
	"""
	Mark a test suite to be included or a function as a test to be ran in the test suite
	"""
	if methodOrClass == None:
		return
	name = methodOrClass.__module__
	if inspect.isclass(methodOrClass):
		clazz = methodOrClass
		TestRunner.tests[clazz] = TestRunner.scanned[name]
		return
	method = methodOrClass
	if name not in TestRunner.scanned:
		initializeTestModule(name)
	if method not in TestRunner.scanned[name]['tests']:
		TestRunner.scanned[name]['tests'][method] = {'skip': False}
	else:
		TestRunner.scanned[name]['tests'][method]['skip'] = False

def skip(methodOrClass: FunctionType):
	"""
	Mark a test suite to be skipped or a function as a test that should be skipped in the test suite 
	"""
	if methodOrClass == None:
		return
	name = methodOrClass.__module__
	if inspect.isclass(methodOrClass):
		clazz = methodOrClass
		for test in TestRunner.scanned[name]['tests']:
			TestRunner.scanned[name]['tests'][test]['skip'] = True
		TestRunner.tests[clazz] = TestRunner.scanned[name]
		return
	method = methodOrClass
	if name not in TestRunner.scanned:
		initializeTestModule(name)
	if method not in TestRunner.scanned[name]['tests']:
		TestRunner.scanned[name]['tests'][method] = {'skip': True}
	else:
		TestRunner.scanned[name]['tests'][method]['skip'] = True

def beforeAll(method: FunctionType):
	"""
	Mark a function in a test suite to be ran first before any tests are ran
	"""
	if method == None:
		return
	moduleName = method.__module__
	if moduleName not in TestRunner.scanned:
		initializeTestModule(moduleName)
	TestRunner.scanned[moduleName]['beforeAll'] = method

def beforeEach(method: FunctionType):
	"""
	Mark a function in a test suite to be ran before each test is ran
	"""
	if method == None:
		return
	moduleName = method.__module__
	if moduleName not in TestRunner.scanned:
		initializeTestModule(moduleName)
	TestRunner.scanned[moduleName]['beforeEach'] = method
