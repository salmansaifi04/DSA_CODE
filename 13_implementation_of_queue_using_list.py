# Queue :- First in First out

class Queue:
    def __init__(self):
        self.mylist = []
    
    def is_empty(self):
        return len(self.mylist) == 0

    def enqueue(self, data):
        self.mylist.append(data)
    
    def dequeue(self):
        if not self.is_empty():
            return self.mylist.pop(0)
        else:
            return "list is empty"

    def get_front(self):
        if not self.is_empty():
            return self.mylist[0]
        else:
            return "list is empty"

    def get_rear(self):
        if not self.is_empty():
            return self.mylist[-1]
        else:
            return "list is empty"
    
    def size(self):
        return len(self.mylist)

myqueue = Queue()
print("Check the Queue is empty or not : ", myqueue.is_empty())
print("size of queue is : ",myqueue.size())
myqueue.enqueue(10)
myqueue.enqueue(20)
myqueue.enqueue(30)
print("size of queue is : ",myqueue.size())
myqueue.dequeue()
print("size of queue is : ",myqueue.size())
print("get front : ",myqueue.get_front())
print("get rear : ",myqueue.get_rear())
