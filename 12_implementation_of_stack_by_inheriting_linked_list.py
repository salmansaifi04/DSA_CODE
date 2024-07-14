from _04_singly_link_list import *

class Stack(SLL):
    # def __init__(self):
    #     self.item_count = 0
    item_count = 0
    def is_empty(self):
        return super().is_empty()
    
    def push(self, data):
        self.insert_at_start(data)
        Stack.item_count += 1
    
    def pop(self):
        if not self.is_empty():
            self.delete_first()
            Stack.item_count -= 1
        
    def peek(self):
        if not self.is_empty():
            return self.start.item
    
    def size(self):
        return Stack.item_count
    
mylist = Stack()
print(mylist.is_empty())
mylist.push(10)
mylist.push(20)
mylist.push(30)
print(mylist.is_empty())
print(mylist.size())
print("top element is : ", mylist.peek())
mylist.pop()
print(mylist.size())
print("top element is : ", mylist.peek())