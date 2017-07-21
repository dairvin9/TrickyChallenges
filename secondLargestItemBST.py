# 7/21/2017

class BinaryTreeNode:

    def __init__(self, value):
        self.value = value
        self.left  = None
        self.right = None

    def insert_left(self, value):
        self.left = BinaryTreeNode(value)
        return self.left

    def insert_right(self, value):
        self.right = BinaryTreeNode(value)
        return self.right
        
    @staticmethod    
    def get_max_and_parent(current):
        temp = current
        parent = None
        while temp.right:
            parent = temp
            temp = temp.right
            
        return (temp,parent)
        
    @staticmethod    
    def get_second_to_last(node):
        (max,parent) = BinaryTreeNode.get_max_and_parent(node)
        if max.left:
            (result,junk) = BinaryTreeNode.get_max_and_parent(max.left)
            return result
        else:
            return parent
            
            
a = BinaryTreeNode(34)
b = BinaryTreeNode(10)
c = BinaryTreeNode(67)
d = BinaryTreeNode(50)

a.left = b
a.right = c
c.left = d 

print(BinaryTreeNode.get_second_to_last(a).value)           