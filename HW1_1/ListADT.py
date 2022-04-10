from abc import ABCMeta, abstractclassmethod, abstractmethod

class MyList(object):
    
    __metaclass__ = ABCMeta
    
    @abstractmethod
    def len(self):
        pass
    
    @abstractmethod
    def getitem(self, j):
        pass
    
    @abstractmethod
    def setitem(self, val, j):
        pass
    
    @abstractmethod
    def insertItem(self, item, j=0):
        pass
    
    @abstractmethod
    def removeItem(self, j=0):
        pass
    
    @abstractmethod
    def printMyList(self):
        pass