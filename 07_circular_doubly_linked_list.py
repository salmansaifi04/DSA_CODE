class Node:
    def __init__(self, item=None,prev=None, next=None):
        self.item = item
        self.prev = prev
        self.next = next


class CDLL:
    def __init__(self, start=None):
        self.start = start

    def is_empty(self):
        return self.start == None
    
    def insert_at_start(self, data):
        n = Node(data)
        if self.is_empty():
            n.next = n
            n.prev = n
        else:
            n.next = self.start
            n.prev = self.start.prev
            self.start.prev.next = n
            self.start.prev = n
        
        self.start = n

    def print_all(self):
        if not self.is_empty():
            print(self.start.item, end= " ")
            temp = self.start.next
            while temp is not self.start:
                print(temp.item, end = " ")
                temp = temp.next

    def insert_at_last(self,data):
        n = Node(data)
        if self.is_empty():
            n.next = n
            n.prev = n
            self.start = n
        else:
            n.prev = self.start.prev
            n.next = self.start
            n.prev.next = n
            self.start.prev = n

    def search(self, data):
        temp = self.start
        if temp == None:
            return None
        
        if temp.item == data:
            return temp
        else:
            temp = temp.next

        while temp != self.start:
            if temp.item == data:
                return temp
            
            temp = temp.next
        
        return None
    
    def insert_after(self, temp, data):
        if temp is not None:
            n = Node(data)
            n.next = temp.next
            n.prev = temp
            temp.next.prev = n
            temp.next = n

    def delete_first(self):
        if self.start is not None:
            if self.start.next == self.start:
                self.start = None
            else:
                self.start.prev.next = self.start.next
                self.start.next.prev = self.start.prev
                self.start = self.start.next

    def delete_last(self):
        if self.start is not None:
            if self.start.next == self.start:
                self.start = None
            else:
                self.start.prev.prev.next = self.start
                self.start.prev = self.start.prev.prev

    def delete_item(self, data):
        if self.start is not None:
            temp = self.start
            if temp.item == data:
                self.delete_first()
            else:
                temp = temp.next
                while temp is not self.start:
                    if temp.item == data:
                        temp.next.prev = temp.prev
                        temp.prev.next = temp.next
                    temp = temp.next

    def __iter__(self):
        return CDLLIterator(self.start)

            
class CDLLIterator:
    def __init__(self, start):
        self.current = start
        self.first = start
        self.count = 0

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current is None:
            raise StopIteration
        if self.current == self.first and self.count == 1:
            raise StopIteration
        else:
            self.count = 1

        data = self.current.item
        self.current = self.current.next
        return data
    
        

mylist = CDLL()
mylist.insert_at_start(10)
mylist.insert_at_start(20)
mylist.insert_at_start(30)
mylist.insert_at_last(5)
# print(mylist.search(10))
mylist.print_all()
print()
mylist.insert_after(mylist.search(5), 50)
mylist.print_all()
# mylist.delete_first()
# mylist.delete_last()
# mylist.delete_item(20)
print()
# mylist.print_all()

for i in mylist:
    print(i)