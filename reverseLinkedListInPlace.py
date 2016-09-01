# Reverse a linked list. In place.
class LinkedListNode:
    def __init__(self, value):
        self.value = value
        self.next  = None
    def __str__(self):
        return self.value
		
def printListNodes(head):
    if head:
        print(head.value)
    if head.next:
        printListNodes(head.next)
	
def reverseInPlace(node):
    prev = None
    while node:
        next = node.next
        node.next = prev
        prev = node
        node = next
    return prev
	
a = LinkedListNode('a') 	
b = LinkedListNode('b')
c = LinkedListNode('c')	
d = LinkedListNode('d')	
a.next = b
b.next = c
c.next = d

#printListNodes(a)
#print(reverseInPlace(a))
printListNodes(reverseInPlace(a))