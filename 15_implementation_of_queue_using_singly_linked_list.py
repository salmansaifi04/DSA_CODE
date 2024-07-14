# Queue :- First in First out

from _04_singly_link_list import *

class Queue:
    def __init__(self):
        self.mylist = SLL()
        self.count_item = 0
    
    def is_empty(self):
        return self.mylist.is_empty()
    
    def enqueue(self, data):
        self.mylist.insert_at_start(data)
        self.count_item += 1
    
    def dequeue(self):
        if not self.is_empty():
            self.count_item -= 1
            return self.mylist.delete_last()

    def get_rear(self):
        if self.mylist.start is not None:
            return self.mylist.start.item
        else:
            return "Queue is empty"
    
    def  get_front(self):
        if self.mylist.start is not None:
            temp = self.mylist.start
            while temp.next is not None:
                temp = temp.next
            return temp.item
        else:
            return "Queue is empty"
    
    def size(self):
        return self.count_item


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