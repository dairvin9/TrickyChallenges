# if I have to implement, ask more about the problem to determine linked list or array implementation

class Stack:
	def __init__(self):
		self.data = []
		
	def push(self, value):
		self.data.append(value)
		
	def pop(self):
		if self.size() == 0:
			raise IndexError('Stack is empty, cannot pop()')
		return self.data.pop()
		
	def top(self):
		if self.size() == 0:
			raise IndexError('Stack is empty, cannot pop()')
		return self.data[-1]
		
	def size(self):
		return len(self.data)
		
class Queue:
	def __init__(self):
		self.data = []
	
	def enqueue(self, value):
		self.data.append(value)
	
	def dequeue(self):
		if self.size() == 0:
			raise IndexError('Stack is empty, cannot pop()')		
		return self.data.pop(0)
		
	def size(self):
		return len(self.data)

	def front(self):
		if self.size() == 0:
			raise IndexError('Stack is empty, cannot pop()')
		return self.data[0]		
        
class SetOfStacks:
    def __init__(self, max_in_a_stack = 5):
        self.stacks = []
        self.max_in_a_stack = max_in_a_stack

    def isFull(self, stack):
        if stack.size() == self.max_in_a_stack:
            return True
        return False    
    
    def push(self, value):
        if len(self.stacks) == 0:
            self.stacks.append(Stack())
        stack = self.stacks[-1]
        if not self.isFull(stack):
            stack.push(value)
        else:
            newStack = Stack()
            newStack.push(value)
            self.stacks.append(newStack)
    
    def pop(self):
        if len(self.stacks) == 0:
            raise IndexError('Stack is empty, cannot pop()')        
        value = self.stacks[-1].pop()
        if self.stacks[-1].size() == 0:
            self.stacks.pop()
        return value    
    
    
"""s = SetOfStacks()
for x in range(100):
    s.push(x)

for y in range (20):
    print(s.pop())"""
    
class MyQueue:
    def __init__(self):
        self.stack1 = Stack()
        self.stack2 = Stack()
        
    def enqueue(self,value):
        self.stack1.push(value)
        
    def dequeue(self):
        if self.stack2.size() > 0:
            return self.stack2.pop()
        elif self.stack1.size() > 0:
            for x in range(self.stack1.size()):
                self.stack2.push(self.stack1.pop())
            return self.stack2.pop()
        else:    
            raise IndexError('Queue is empty, cannot pop()') 

"""a = MyQueue()
for x in range(5):
    a.enqueue(x)
for y in range(6):
    print(a.dequeue())"""
    
class TowerOfHanoi:
    a = Stack()
    b = Stack()
    c = Stack()
    
    def __init__(self, size):
        for x in range(size,0,-1):
            a.push(x)
        
        self.size = size
    
    def move(self,s1,s2):
        if s2.size() == 0 or s1.top() < s2.top():
            s2.push(s1.pop())
        elif:
            print('cannot move element')
    
    def solve(self):
        if a.size() == 0 and b.size() == 0 and c.size() == self.size:
            return True
            