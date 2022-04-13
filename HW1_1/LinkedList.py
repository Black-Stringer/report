from ListADT import MyList

class Node(object):
    
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node
        
    def get_data(self):
        return self.data
    
    def set_data(self, data):
        self.data = data
        
    def get_next(self):
        return self.next_node
    
    def set_next(self, new_next):
        self.next_node = new_next
        
class LinkedList(MyList):
    
    def __init__(self, head=None):
        self.head = None
        self.length = 0
        
    def len(self):
        return self.length
    
    def getitem(self, j):
        curr = self.head
        for i in range(j):
            curr = curr.get_next()
            
        return curr
    
    def setitem(self, val, j):
        self.getitem(j).set_data(val)
    
    def insertItem(self, item, j=0):
        newNode = Node(item)
        if self.head == None: self.head = newNode
        else:
            curr = self.getitem(j-1)

            if j == 0:
                self.head = newNode
                newNode.set_next(curr)
            else:
                newNode.set_next(curr.get_next())
                curr.set_next(newNode)

        self.length += 1
    
    def removeItem(self, j=0):
        curr = self.getitem(j)

        if j == 0:
            self.head = curr.get_next()
            del curr
        else:
            self.getitem(j-1).set_next(curr.get_next())
            del curr

        self.length -= 1
    
    def printMyList(self):
        curr = self.head    
        while curr is not None:
            print(curr.get_data(), end=' ')
            curr = curr.get_next()
        print("\n")
    
myLinkedList = LinkedList()

myLinkedList.insertItem(4)
myLinkedList.insertItem(3)
myLinkedList.insertItem(1)
myLinkedList.insertItem(2,1)

myLinkedList.printMyList()

myLinkedList.removeItem(3)
myLinkedList.removeItem(1)
myLinkedList.removeItem(0)

myLinkedList.printMyList()