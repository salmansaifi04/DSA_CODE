# Binary Search Tree

class Node:
    def __init__(self, item=None, left=None, right=None):
        self.item = item
        self.left = left
        self.right = right
    
class BST:
    def __init__(self, root=None):
        self.root = root
    
    def insert(self, data):
        self.root = self.rinsert(self.root, data)

    def rinsert(self, root, data):
        if root is None:
            return Node(data)
        
        if data < root.item:
            root.left = self.rinsert(root.left, data)
        
        elif data > root.item:
            root.right = self.rinsert(root.right, data)

        return root
    
    def search(self, data):
        return self.rsearch(self.root, data)
    
    def rsearch(self, root, data):
        if root is None or root.item == data:
            return root
        
        if data<root.item:
            return self.rsearch(root.left, data)
        else:
            return self.rsearch(root.right, data)
        
    def inorder(self):
        result = []
        self.rinorder(self.root, result)
        return result
    
    def rinorder(self, root, result):
        # in inorder search (left, root, right)
        if root:
            self.rinorder(root.left, result)
            result.append(root.item)
            self.rinorder(self.right, result)

    def preorder(self):
        result = []
        self.rpreorder(self.root, result)
        return result
    
    def rpreorder(self, root, result):
        # in preorder search (root ,left, right)
        if root:
            result.append(root.item)
            self.rpreorder(root.left, result)
            self.rpreorder(self.right, result)

    def postorder(self):
        result = []
        self.rpostorder(self.root, result)
        return result
    
    def rpostorder(self, root, result):
        # in postorder search (left, right, root)
        if root:
            self.rpostorder(root.left, result)
            self.rpostorder(self.right, result)
            result.append(root.item)

mybst_obj = BST()
mybst_obj.insert(50)
mybst_obj.insert(40)
mybst_obj.insert(30)
mybst_obj.insert(60)
print(mybst_obj.inorder())

