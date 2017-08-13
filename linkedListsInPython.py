import math

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def __repr__(self):
        return 'Node ' + str(self.value) 
        
class LinkedList:
    @staticmethod
    def printLinkedList(node):
        while node:
            print(node.value)
            node = node.next

e = Node(5)
d = Node(4,e)
c = Node(3,d)
b = Node(2,c)

z = Node(5)
y = Node(4,z)
x = Node(3,y)
w = Node(2,x)

def addTwoLinkedLists(list1, list2):
    # cases:
    # add and nothing carries over
    # add and a carry over
    # one node could be empty
    # both nodes are empty and there is a carry over
    head = list1 # for returning
    current1 = list1
    current2 = list2
    
    if current1 is None:
        return current2
    
    carryOver = 0
    while current1:
        if current2:
            sum = current1.value + current2.value + carryOver
            current1.value = sum % 10
            carryOver = math.floor(sum / 10)
            
            if current1.next is None:
                if current2.next:
                    current2.value = current2.next.value + carryOver
                    current1.next = current2.next
                    break
                else:
                    current1.next = Node(1)
                    break
            current1 = current1.next
            current2 = current2.next

        else:
            current1.value = current1.value + carryOver
            break
            
    return head
    
"""LinkedList.printLinkedList(addTwoLinkedLists(w,b))"""  

# assuming that the 0th to last element is the last element
def getNthToLastElement(head, n):
    if n < 0:
        return ValueError('Parameter n must be 0 or greater, found ' + str(n))
    
    n = n + 1 
    current = head
    runner = head
    for count in range(n):
        runner = runner.next
        
    while runner:
        runner = runner.next
        current = current.next
    return current.value        

#print(getNthToLastElement(b,0))
#print(getNthToLastElement(b,3))        
        
def removeDuplicatesFromLinkedList(head):
    seen = set()
    if head is None:
        return None
        
    current = head
    seen.add(current.value)
    while current.next:
        if current.next.value in seen:
            current.next = current.next.next
        else:
            seen.add(current.next.value)
            current = current.next
    
    return head

"""LinkedList.printLinkedList(removeDuplicatesFromLinkedList(c))
LinkedList.printLinkedList(removeDuplicatesFromLinkedList(b))"""
    
# case, first element in list, last, somewhere in teh middle        
# deletes a certain value        
def deleteFromLinkedList(current, value):
    head = current
    
    if current is None:
        return None # could also throw type or value error
    if current.value == value:
        return current.next
    while current.next is not None:
        if current.next.value == value:
            current.next = current.next.next          
            return head
        current = current.next
    
    raise ValueError('Value not found in linked list.')




"""LinkedList.printLinkedList(deleteFromLinkedList(c,4))
try:
    deleteFromLinkedList(c,10)    
except Exception as e:
    print(e)"""