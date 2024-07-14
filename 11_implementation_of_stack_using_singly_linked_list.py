from _04_singly_link_list import *

class Stack:
    def __init__(self):
        self.mylist = SLL()
        self.count_item = 0

    def is_empty(self):
        return self.mylist.is_empty()
    
    def push(self, data):
        self.mylist.insert_at_start(data)
        self.count_item += 1
    
    def pop(self):
        if not self.is_empty():
            self.mylist.delete_first()
            self.count_item -= 1
    
    def peek(self):
        if not self.is_empty():
            print(self.mylist.start.item)
        else:
            raise IndexError("Stack is empty")
    
    def size(self):
        return self.count_item
    
mylist_obj = Stack()
# print(mylist_obj.is_empty())
mylist_obj.push(10)
mylist_obj.push(20)
mylist_obj.peek()
print(mylist_obj.size())