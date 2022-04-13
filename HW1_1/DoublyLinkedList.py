from ListADT import MyList

class Node(object):
    
    def __init__(self, data=None, next_node=None, previous_node=None):
        self.data = data
        self.next_node = next_node
        self.previous_node = previous_node
        
    def get_data(self):
        return self.data
    
    def set_data(self, data):
        self.data = data
        
    def get_next(self):
        return self.next_node
    
    def set_next(self, new_next):
        self.next_node = new_next
    
    def get_previous(self):
        return self.previous_node
    
    def set_previous(self, new_previous):
        self.previous_node = new_previous

class DoublyLinkedList(MyList):
    
    def __init__(self, header=None, tailer=None):
        self.header = None
        self.tailer = None
        self.length = 0
    
    def len(self):
        return self.length
    
    def getitem(self, j):
        curr = self.header
        for i in range(j):
            curr = curr.get_next()
            
        return curr
    
    def setitem(self, val, j):
        self.getitem(j).set_data(val)
    
    def insertItem(self, item, j=0):
        newNode = Node(item)
        if self.header == None: self.header = newNode
        else:
            curr = self.getitem(j-1)
                
            if j == 0:
                self.header = newNode
                newNode.set_next(curr)
                curr.set_previous(newNode)
            else:
                newNode.set_next(curr.get_next())
                newNode.set_previous(curr)
                curr.get_next().set_previous(newNode)
                curr.set_next(newNode)
                
            while curr.get_next() is not None:
                curr = curr.get_next()
            self.tailer = curr

        self.length += 1
    
    def removeItem(self, j=0):
        curr = self.getitem(j)
        
        if j == 0:
            self.header = curr.get_next()
            curr.set_data(None)
        else:
            if self.tailer is not curr:
                curr.get_next().set_previous(curr.get_previous())
            if self.header is not curr:
                curr.get_previous().set_next(curr.get_next())
            curr.set_data(None)
            
        self.length -= 1
    
    def printMyList(self):
        curr = self.header
        while curr is not None:
            print(curr.get_data(), end=' ')
            curr = curr.get_next()
        print("\n")
    
myDoublyLinkedList = DoublyLinkedList()

myDoublyLinkedList.insertItem(4)
myDoublyLinkedList.insertItem(3)
myDoublyLinkedList.insertItem(1)
myDoublyLinkedList.insertItem(2,1)

myDoublyLinkedList.printMyList()

myDoublyLinkedList.removeItem(3)
myDoublyLinkedList.removeItem(1)
myDoublyLinkedList.removeItem(0)

myDoublyLinkedList.printMyList()