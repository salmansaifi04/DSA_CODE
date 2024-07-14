# Stack :- Last in First out

class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0
    
    def push(self, data):
        self.items.append(data)

    def pop(self):
        if not self.is_empty():
            popped_items = self.items.pop()
            return f"popped items is {popped_items}"
        else:
            raise IndexError("Stack is Empty")

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError("Stack is Empty")
    
    def size(self):
        return len(self.items)
    

mystack = Stack()
# print(mystack.is_empty())
# mystack.push(20)
# mystack.push(30)
# mystack.push(40)
# print(mystack.peek())
# mystack.pop()
# mystack.peek()
# print(mystack.size())