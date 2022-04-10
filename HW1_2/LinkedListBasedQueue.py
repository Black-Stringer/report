from QueueADT import MyQueue

class Node(object):
    
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node
        
    def get_data(self):
        return self.data
    
    def get_next(self):
        return self.next_node
    
    def set_next(self, new_next):
        self.next_node = new_next
        
class LinkedListBasedQueue(MyQueue):
    
    def __init__(self, head=None):
        self.head = None
        self.length = 0
        
    def len(self):
        return self.length
    
    def first(self):
        return self.head.get_data()
    
    def is_empty(self):
        if self.len() == 0: return True
        else: return False
    
    def enqueue(self, item):
        newNode = Node(item)
        if self.length == 0:
            self.head = newNode
        else:
            curr = self.head
            while curr.get_next() is not None:
                curr = curr.get_next()
            curr.set_next(newNode)
                
        self.length += 1
    
    def dequeue(self):
        
        try:
            curr = self.head
            self.head = self.head.get_next()
            curr.data = None
            curr.set_next(None)
        
            self.length -= 1
        except AttributeError:
            print("The queue is empty so cannot dequeue.\n")
    
    def printMyQueue(self):
        curr = self.head
        while curr is not None:
            print("{}".format(curr.get_data()), end=" ")
            curr = curr.get_next()
        print("\n")
    
q = LinkedListBasedQueue()

q.enqueue(5)
q.enqueue(3)

q.printMyQueue()
print("A length of queue is {}\n".format(q.is_empty()))

q.dequeue()
q.dequeue()
print("The queue is empty: {}\n".format(q.is_empty()))

q.dequeue()

q.enqueue(7)
q.enqueue(9)
print("A first element of queue is {}\n".format(q.first()))