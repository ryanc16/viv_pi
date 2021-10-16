from __future__ import annotations
from typing import List

class InputReportingService:

  _instance = None
  def __init__(self):
    if InputReportingService._instance is not None:
      raise TypeError("Cannot instantiate singleton")
    self.valueDict = dict()

  def instance() -> InputReportingService:
    if InputReportingService._instance is None:
      InputReportingService._instance = InputReportingService()
    return InputReportingService._instance

  def report(self, inputId: str, value: object):
    self.valueDict[inputId] = value
  
  def check(self, inputId: str):
    return self.valueDict.get(inputId)

  def checkAll(self, inputIds: List[str]):
    results = list()
    for inputId in inputIds:
      results.append(self.valueDict.get(inputId))
    return results