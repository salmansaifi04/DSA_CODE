class Node:
    def __init__(self, item=None, next = None):
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
        else:
            temp = self.start
            while temp.next is not None:
                temp = temp.next
            temp.next = n
    
    def find_middle(self):
        v = []
        temp = self.start
        while temp is not None:
            v.append(temp.item)
            temp = temp.next
        
        middle_value = len(v)//2
        return v[middle_value]
    
    def print_all(self):
        temp = self.start
        while temp is not None:
            print(temp.item, end=" ")
            temp = temp.next

    

s1 = SLL()
s1.insert_at_last(10)
s1.insert_at_last(20)
s1.insert_at_last(30)
s1.insert_at_start(5)
s1.insert_at_start(7)
print(s1.find_middle())
s1.print_all()