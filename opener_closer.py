"""
Let's say:

	'(', '{', '[' are called "openers."
	')', '}', ']' are called "closers."
	Write an efficient function that tells us whether or not an input string's openers and closers are properly nested.

""" 

# Cute stack class idea from http://stackoverflow.com/questions/4688859/stack-data-structure-in-python
class stack(list):
    def push(self, item):
        self.append(item)
    def isEmpty(self):
        return not self
        
# Returns false { [ ( ] ) }
# Returns true  { [ ] ( ) }   


# look at every character,. so at best O(n)
# loop straight through. store the openers in a way that takes what you see now and puts it on top. And for closerrs take out and matcho ut what is on top. WE NEED A STACK!
def bracket_validator(line):
    s = stack()
    for n in line:
        if n == '{' or n == '[' or n == '(':
            s.push(n)
        else:
            try:    
                if n == '}':
                    if s.pop() != '{':
                        return False
                elif n == ']':
                    if s.pop() != '[':
                        return False
                elif n == ')':
                    if s.pop() != '(':
                        return False
            except ValueError:
                return False
            except:
                raise error
    
    if s.isEmpty():
        return True    
    return False
    
def testing():
    # IF the code is good, should be all Trues
    print bracket_validator(" { [ ( ] ) }") == False
    print bracket_validator("{ [ ] ( ) }") == True
    
testing()    
     