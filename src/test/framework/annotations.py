from src.test.framework.test import Test
from types import FunctionType

def test(method: FunctionType):
	if method == None:
		return
	if method.__module__ not in Test.tests:
		Test.tests[method.__module__] = {}
	if method not in Test.tests[method.__module__]:
		Test.tests[method.__module__][method] = {'skip': False}

def skip(method: FunctionType):
	if method == None:
		return
	if method.__module__ not in Test.tests:
		Test.tests[method.__module__] = {}
	Test.tests[method.__module__][method] = {'skip': True}