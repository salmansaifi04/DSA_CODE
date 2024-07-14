class Node:
    def __init__(self, item= None, next = None):
        self.item = item
        self.next = next

class SLL:
    def __init__(self, start=None):
        self.start = start

    def insert_at_start(self, data):
        n = Node(data, self.start)
        self.start = n

    def insert_at_last(self, data):
        n = Node(data)
        if self.start == None:
            self.start = n
        elif self.start.next == None:
            self.start.next = self.start
            self.start = n
        else:
            temp = self.start
            while temp.next is not None:
                temp = temp.next
            
            temp.next = n

    def reverse_linked_list(self):
        if self.start == None:
            return self.start
        elif self.start.next == None:
            return self.start.item , self.start
        else:
            temp = self.start
            while temp.next is not None:
                pass




        
