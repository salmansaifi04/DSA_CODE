# Queue :- First in First out

class Queue(list):
    def is_empty(self):
        return len(self) == 0
    
    def enqueue(self, data):
        self.append(data)
    
    def dequeue(self):
        self.pop(0)
    
    def get_front(self):
        if not self.is_empty():
            return self[0]
        else:
            return "Queue is empty"
    
    def get_rear(self):
        if not self.is_empty():
            return self[-1]
        else:
            return "Queue is empty"
    
    def size(self):
        return len(self)
    
    def insert(self, index=0, data=0):
        raise AttributeError("You can't use insert method in Queue")


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


    