"""Doubly linked list"""

class Node:
    def __init__(self, prev=None, item=None, next=None):
        self.prev = prev
        self.item = item
        self.next = next


class DLL:
    def __init__(self, start=None):
        self.start = start

    def is_empty(self):
        return self.start == None

    def insert_at_first(self, data):
        n = Node(None, data, self.start)
        if not self.is_empty():
            self.start.prev = n
        self.start = n

    def insert_at_last(self, data):
        temp = self.start
        n = Node(None, data)
        if temp is None:
            self.start = n
        elif temp.next is None:
            self.start.prev = self.start
            temp.next = n
        else:
            while temp.next != None:
                temp = temp.next
            temp.next = n
            temp.next.prev = temp
        
    def search(self, data):
        temp = self.start
        if temp is None:
            pass
        elif temp is not None:
            while temp is not None:
                if temp.item == data:
                    return temp
                temp = temp.next

    def insert_after(self, data, temp):
        if self.search(temp):
            n = Node(self.search(temp), data, self.search(temp).next)
            self.search(temp).next = n
            
    def printall(self):
        if self.start is not None:
            temp = self.start
            while temp is not None:
                print(temp.item, end=" ")
                temp = temp.next

    def delete_first(self):
        if self.start is not None:
            self.start = self.start.next
            if self.start is not None: 
                self.start.prev = None
    
    def delete_last(self):
        temp = self.start
        if temp.next is None:
            self.start = None
        else:
            while temp.next.next is not None:
                temp = temp.next

            temp.next = None
    
    def delete_item(self, data):
        
        if self.start is not None:
            if self.start.item == data:
                self.start = self.start.next
                if self.start is not None:
                    self.start.prev = None
            else:
                temp = self.start
                while temp.next is not None:
                    if temp.next.item == data:
                        temp.next = temp.next.next
                        if temp.next is not None:
                            temp.next.prev = temp
                        break
                    temp = temp.next
    
    def __iter__(self):
        return DLLIterator(self.start)
            

class DLLIterator:
    def __init__(self, start):
        self.current = start
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if not self.current:
            raise StopIteration
        
        data = self.current.item
        self.current = self.current.next
        return data

mylist = DLL()
mylist.insert_at_first(10)
mylist.insert_at_first(20)
# mylist.insert_at_first(20)
# mylist.insert_at_first(20)
# mylist.insert_at_first(20)
# mylist.insert_at_last(5)
mylist.insert_after(5, 20)
# mylist.delete_first()
# mylist.delete_last()
mylist.delete_item(5)
mylist.printall()
# mylist.search(5)

# for i in mylist:
#     print(i)