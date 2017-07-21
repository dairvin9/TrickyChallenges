class Stack:
    
    # initialize an empty list
    
    
    def __init__(self):
        self.items = []
  
    # push a new item to the last index
    def push(self, item):
        self.items.append(item)
        

    # remove the last item
    def pop(self):
        # if the stack is empty, return None
        # (it would also be reasonable to throw an exception)
        if not self.items: 
            return None       
        return self.items.pop()
        
    # see what the last item is
    def peek(self):
        if not self.items: 
            return None
        return self.items[-1]

class MaxStack:
    def __init__(self):
        self.s = Stack()
        self.max = Stack()
    
    def push(self, item):
        self.s.push(item)
        if not self.max.peek() or item > self.max.peek():
            self.max.push(item)
            
    def pop(self):
        item = self.s.pop()

        if item == self.max.peek():
            self.max.pop()
        return item 
        
    def peek(self):
        return self.s.peek()
        
    def getMax(self):
        return self.max.peek()

a  = MaxStack()
a.push(3)
print(a.getMax())   
a.push(4)
print(a.getMax())   
a.push(2)
print(a.getMax())   
a.push(6)
print(a.getMax())   
a.pop()
print(a.getMax())   
a.pop()
print(a.getMax())   
a.pop()
print(a.getMax())  