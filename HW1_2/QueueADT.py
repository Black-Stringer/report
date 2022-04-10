from abc import ABCMeta, abstractmethod

class MyQueue(object):
    
    __metacalss__ = ABCMeta
    
    @abstractmethod
    def len(self):
        pass
    
    @abstractmethod
    def first(self):
        pass
    
    @abstractmethod
    def is_empty(self):
        pass
    
    @abstractmethod
    def enqueue(self, item):
        pass
    
    @abstractmethod
    def dequeue(self, j=0):
        pass
    
    @abstractmethod
    def printMyQueue(self):
        pass