# string all unique characters

unique = "henry"
notUnique = "denise"

# Assumptions:
# upper and lower are unique
# empty string throw ValueError
# ascii or unicode? python 3 handles unicode (yay)

# with additional structures:
def isUnique(s):
    if type(s) != str:
        raise TypeError('Function isUnique requires nonempty string, found ' + str(type(s)))
    if len(s) == 0:
        raise ValueError('Function isUnique requires nonempty string, found empty string')
    
    chars = set()
    for char in s:
        if char in chars:
            return False
        chars.add(char)
    return True

def isUniqueNoAdditionalStructures(s):
    if type(s) != str:
        raise TypeError('Function isUniqueNoAdditionalStructures requires nonempty string, found ' + str(type(s)))
    if len(s) == 0:
        raise ValueError('Function isUniqueNoAdditionalStructures requires nonempty string, found empty string')
    
    for index in range(0,len(s)):
        for current_index in range(index + 1,len(s)):
            if s[index] == s[current_index]:
                return False
    return True            
    
# a third option is to sort it and walk through that if we can destroy input string.     
    
# runs in O(n), takes up O(n) space
print(isUniqueNoAdditionalStructures(unique))
print(isUniqueNoAdditionalStructures(notUnique))    
try:
    isUniqueNoAdditionalStructures(4)
except Exception as e:
    print(e)
    
try:
    isUniqueNoAdditionalStructures('')
except Exception as e:
    print(e)
    
