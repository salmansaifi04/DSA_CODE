# Stack :- Last in first out

class Stack(list):
    def is_empty(self):
        return len(self)==0
    
    def push(self, data):
        self.append(data)

    def pop(self):
        if not self.is_empty():
            return super().pop()
        else:
            raise IndexError("Stack is empty")

    def peek(self):
        if not self.is_empty():
            return self[-1]
        else:
            raise IndexError("Stack is empty")
    
    def size(self):
        return len(self)
    
    def insert(self, index=0, data=0):
        raise AttributeError("You can't use insert method in stack")



s1 = Stack()
s1.push(10)
s1.push(20)
s1.push(30)
print(s1.is_empty())
print("popped item is ", s1.pop())
print("top item is ", s1.peek())
print("size of stack is ", s1.size())
s1.insert()