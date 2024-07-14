class Deque:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0
    
    def insert_front(self, data):
        self.items.insert(0, data)
    
    def insert_rear(self, data):
        self.items.append(data)
    
    def delete_front(self):
        if not self.is_empty():
            self.items.pop(0)
        else:
            return "Deque is empty"
    
    def delete_rear(self):
        if not self.is_empty():
            self.items.pop()
        else:
            return "Deque is empty"
    
    def get_front(self):
        if not self.is_empty():
            return self.items[0]
        else:
            return "Deque is empty"
    
    def get_rear(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            return "Deque is empty"
    
    def size(self):
        return len(self.items)

mylist = Deque()
# print(mylist.is_empty())
mylist.insert_front(10)
mylist.insert_front(20)
mylist.insert_rear(30)
print(mylist.size())
print(mylist.delete_front())
print(mylist.delete_rear())
print(mylist.get_rear())
print(mylist.get_front())