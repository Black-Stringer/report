from ListADT import MyList

class ArrayBasedList(MyList):
    
    length = 0
    
    def __init__(self, size):
        self.item = size*[None]
        self.length = 0
        
    def len(self):
        return self.length
    
    def getitem(self, j):
        if self.length > j:
            return self.item[j]
        raise ValueError('Value not in list')
    
    def setitem(self, val, j):
        if self.length > j:
            self.item[j] = val
            return
        raise ValueError('index is out of bound')
    
    def insertItem(self, item, j=0):
        self.length += 1
        
        for i in range(self.len()-1, j, -1):
            self.setitem(self.getitem(i-1), i)

        self.setitem(item, j)
    
    def removeItem(self, j=0):
        self.setitem(None, j)
        
        for i in range(j, self.len()-1):
            self.setitem(self.getitem(i+1), i)
            
        self.setitem(None, self.len()-1)
        self.length -= 1
    
    def printMyList(self):
        for i in range(self.len()):
            print("{} ".format(self.getitem(i)), end=' ')
        print("\n")
    
tenSizeList = ArrayBasedList(10)

tenSizeList.insertItem(4)
tenSizeList.insertItem(3)
tenSizeList.insertItem(1)

tenSizeList.insertItem(2, 1)
tenSizeList.printMyList()

tenSizeList.removeItem(3)
tenSizeList.removeItem(1)
tenSizeList.removeItem(0)

tenSizeList.printMyList()
