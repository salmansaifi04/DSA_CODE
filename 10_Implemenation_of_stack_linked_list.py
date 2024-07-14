class Node:
    def __init__(self, item=None, next=None):
        self.item = item
        self.next = next

class Stack:
    def __init__(self):
        self.start = None
        self.item_count = 0

    def is_empty(self):
        return self.start == None
    
    def push(self, data):
        n = Node(data)
        if not self.is_empty():
            n.next = self.start
            self.start = n
        else:
            self.start = n
        self.item_count += 1
    
    def pop(self):
        if not self.is_empty():
            rm_var = self.start.item
            self.start = self.start.next
            self.item_count -= 1
            return rm_var
        else:
            raise IndexError("Stack is empty")
        
    def peek(self):
        if not self.is_empty():
            print(self.start.item)
        else:
            raise IndexError("Stack is empty")

    def size(self):
        return self.item_count
        
s1 = Stack()
s1.push(10)
s1.push(20)
s1.push(30)
s1.push(40)
# print(s1.is_empty())
# s1.size()
# print(s1.item_count)
# print(s1.pop())
print("size of stack is ", s1.size())
# print(s1.item_count)
s1.peek()