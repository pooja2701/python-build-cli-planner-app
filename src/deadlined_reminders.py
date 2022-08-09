from abc import ABC, ABCMeta, abstractmethod
from collections.abc import Iterable
from dateutil.parser import parse 
from datetime import datetime 

class DeadlineMetaReminder(Iterable, metaclass=ABCMeta=ABCMeta):
  
  @abstractmethod
  def is_due(self):
      pass
class DeadReminder(DeadlineReminder):
  def __init__(self, text, date):
    self.date = parse(date, dayfirst=True)
    self.text = text
  
  def is_due(self):
    return self.date<= datetime.now()
  
  def __iter__(self):
    return iter([self.text, self.date.isoformat()])
