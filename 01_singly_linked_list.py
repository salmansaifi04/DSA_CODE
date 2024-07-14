class Node:
    def __init__(self, item=None, next=None):
        self.item = item
        self.next = next

class SLL:
    def __init__(self, start=None):
        self.start = start

    def is_empty(self):
        return self.start == None
    
    def insert_at_start(self, data):
        n = Node(data, self.start)
        self.start = n
        
    def insert_at_last(self, data):
        n = Node(data)
        if self.is_empty():
            self.start = n
        else:
            temp = self.start
            while temp.next is not None:
                temp = temp.next
            temp.next = n
    
    def search(self, data):
        if self.is_empty():
            print("Singly linked list is empty")
            return None
        else:
            temp = self.start
            while temp is not None:
                if temp.item == data:
                    return temp
                temp = temp.next
            return None

    def delete_first(self):
        if self.is_empty():
            return "Singly linked list is empty"
        self.start = self.start.next
    
    def delete_last(self):
        if self.is_empty():
            return "Singly linked list is empty"
        else:
            temp = self.start
            while temp.next.next is not None:
                temp = temp.next
            temp.next = None
    
    def delete_element(self, data):
        if self.is_empty():
            return "Singly linked list is empty"
        else:
            if self.start.next is None:
                if self.start.item == data:
                    self.start = None
            else:
                temp = self.start
                if temp.item == data:
                    self.start = temp.next
                else:
                    while temp.next is not None:
                        if temp.next.item == data:
                            temp.next = temp.next.next
                            break
                        temp = temp.next

    
    def print_list(self):
        temp = self.start
        while temp:
            print(temp.item)
            temp = temp.next

s1 = SLL()
s1.insert_at_start(10)
s1.insert_at_last(30)
s1.insert_at_start(20)
s1.print_list()
# print("---------------")
# s1.delete_first()
# s1.print_list()
# print("---------------")
# s1.delete_last()
# s1.print_list()
print("--------------")
s1.delete_element(20)
s1.print_list()   
