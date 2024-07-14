class Node:
    def __init__(self, item=None, next=None):
        self.item = item
        self.next = next

class Queue:
    def __init__(self):
        self.start = None
        self.item_count = 0

    def is_empty(self):
        return self.start == None
    
    def enqueue(self, data):
        n = Node(data, self.start)
        self.start = n
        self.item_count += 1
    
    def dequeue(self):
        if not self.is_empty():
            temp = self.start
            while temp.next.next is not None:
                temp = temp.next
            temp.next = None
            self.item_count -= 1
        else:
            return "Queue is empty"
    
    def get_front(self):
        if not self.is_empty():
            temp = self.start
            while temp.next is not None:
                temp = temp.next
            return temp.item
        else:
            return "Queue is empty"

    def get_rear(self):
        if not self.is_empty():
            return self.start.item
        else:
            return "Queue is empty"
        
    def size(self):
        return self.item_count
    

myqueue = Queue()
print("checking the queue is empty or not : ",myqueue.is_empty())
myqueue.enqueue(10)
myqueue.enqueue(20)
myqueue.enqueue(30)
print("size of the Queue is : ", myqueue.size())
myqueue.dequeue()
print("size of the Queue is : ", myqueue.size())
print("get front : ", myqueue.get_front())
print("get rear : ", myqueue.get_rear())

