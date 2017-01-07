class Node:    
    __slots__ = ['numComplete', 'children','parent']
    def __init__(self):
        self.children = {}
        self.numComplete = 0
        self.parent = None

    
class Trie:
    def __init__(self):
        self.root = Node()
        
    def insert(self,contact):    
        letter_index = 0
        current = self.root
        while letter_index < len(contact):
            if contact[letter_index] in current.children:
                current = current.children[contact[letter_index]]
                letter_index+=1
            else:
                current.children[contact[letter_index]] = Node()
                current.children[contact[letter_index]].parent = current
                current = current.children[contact[letter_index]]      
                letter_index+=1
        while current.parent:
            current.numComplete += 1
            current = current.parent
        return
    
    def find(self,contact):
        current_node = self.root
        for letter in contact:
            if letter in current_node.children:
                current_node = current_node.children[letter]
            else:
                return 0
        return current_node.numComplete 
        
                    
myTrie = Trie()
n = int(input().strip())
for a0 in range(n):
    op, contact = input().strip().split(' ')
    if op == 'add':
        myTrie.insert(contact)
    elif op == 'find':
        print(myTrie.find(str(contact)))