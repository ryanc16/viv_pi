from src.test.framework.test_runner import TestRunner


class BaseMock:

  def __init__(self, class_instance: object, method: str):
    self._original_class = class_instance
    self._original_method = method
    self._original_func = getattr(class_instance, method)
    self._calls = []

  def reset(self):
    self._calls = []

  def restore(self):
    setattr(self._original_class, self._original_method, self._original_func)

class MockFn(BaseMock):

  def __init__(self, class_instance: object, method: str):
    super().__init__(class_instance, method)
    setattr(class_instance, method, lambda *args: self._invoke(*args))
    self._mockAction = None
    self._returnVal = None

  def _invoke(self, *args):
    returnVal = None
    if self._mockAction is not None:
      returnVal = self._mockAction.__call__(*args)
    if returnVal is None:
      returnVal = self._returnVal
    self._calls.append((args, returnVal))
    return returnVal

  def thenDo(self, fn):
    self._mockAction = lambda *args: fn.__call__()
    return self

  def thenReturn(self, value):
    self._returnVal = value

class SpyFn(BaseMock):
  def __init__(self, class_instance: object, method: str):
    super().__init__(class_instance, method)
    setattr(class_instance, method, lambda *args: self._invoke(*args))

  def _invoke(self, *args):
    returnVal = self._original_func.__call__(*args)
    self._calls.append((args, returnVal))
    return returnVal

class MockAssertion:
  def __init__(self, mock: BaseMock):
    self.mock = mock

  def toHaveBeenCalled(self) -> bool:
    assert len(self.mock._calls) > 0, f"Expected {self.mock.original_class.__name__}.{self.mock.original_method} to have been called"

  def toHaveBeenCalledTimes(self, times: int) -> bool:
    assert len(self.mock._calls) == times, f"Expected {self.mock.original_class.__name__}.{self.mock.original_method} to have been called {times} times, but was actually called {len(self.mock._calls)} times"
  
  def toHaveBeenCalledWith(self, arg) -> bool:
    calls = list(map(lambda invocation: invocation[0], self.mock._calls))
    assert arg in calls, f"Expected {self.mock.original_class.__name__}.{self.mock.original_method} to have been called with {arg}.\nActual calls include {calls}"

  def toHaveLastBeenCalledWith(self, arg) -> bool:
    call = list(map(lambda invocation: invocation[0], self.mock._calls))[len(self.mock._calls)-1]
    assert call == arg, f"Expected {self.mock.original_class.__name__}.{self.mock.original_method} to have last been called with {arg}.\nActual last call was {call}"

  def toHaveReturned(self, value) -> bool:
    calls = list(map(lambda invocation: invocation[1], self.mock._calls))
    assert value in calls, f"Expected {self.mock.original_class.__name__}.{self.mock.original_method} to have returned {value}.\nActual returned values include {calls}"

  def toHaveLastReturned(self, value) -> bool:
    call = list(map(lambda invocation: invocation[1], self.mock._calls))[len(self.mock._calls)-1]
    assert call == value, f"Expected {self.mock.original_class.__name__}.{self.mock.original_method} to have last returned {value}.\nActual last returned value was {call}"

def mock(class_instance: object, method: str):
  mock = MockFn(class_instance, method)
  TestRunner.mocks.append(mock)
  return mock

def spyOn(class_instance: object, method: str):
  spy = SpyFn(class_instance, method)
  TestRunner.mocks.append(spy)
  return spy

def assertMock(mock) -> MockAssertion:
  return MockAssertion(mock)