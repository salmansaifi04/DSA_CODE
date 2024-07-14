class Node:
    def __init__(self, item=None, next=None, prev=None):
        self.item = item 
        self.next = next
        self.prev = prev

class Deque:
    def __init__(self):
        self.front = None
        self.rear = None
        self.item_count = 0

    def is_empty(self):
        return self.item_count == 0

    def insert_front(self, data):
        n = Node(data, self.front, None)
        if self.is_empty():
            self.rear = n
        else:
            self.front.prev = n
        self.front = n
        self.item_count += 1
    
    def insert_rear(self, data):
        n = Node(data, None, self.rear)
        if self.is_empty():
            self.front = n
        else:
            self.rear.next = n
        self.rear = n
        self.item_count += 1

    def delete_front(self):
        if self.is_empty():
            return "Deque is empty"
        if self.front == self.rear:
            self.front = None
            self.rear = None
        else:
            self.front = self.front.next
            self.front.prev = None
        self.item_count -= 1
    
    def delete_rear(self):
        if self.is_empty():
            return "Deque is empty"
        if self.front == self.rear:
            self.front = None
            self.rear = None
        else:
            self.rear = self.rear.prev
            self.rear.next = None
        self.item_count -= 1

    def get_front(self):
        if self.is_empty():
            return "Deque is empty"
        else:
            return self.front.item
    
    def get_rear(self):
        if self.is_empty():
            return "Deque is empty"
        else:
            return self.rear.item
    
    def size(self):
        return self.item_count

mylist = Deque()
# print(mylist.is_empty())
mylist.insert_front(10)
mylist.insert_front(20)
mylist.insert_rear(30)
print(mylist.size())
# print(mylist.delete_front())
# print(mylist.delete_rear())
print(mylist.get_rear())
print(mylist.get_front())
        
