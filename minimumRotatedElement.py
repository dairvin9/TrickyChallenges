# if an array is sorted, and is then rotated, find the minimum element.
# python 3
import math


ex1 = [5, 6, 7, 8, 9, 10, 11, 1, 2, 3, 4]
ex2 = [5, 1, 2, 3, 4]
ex3 = [5]
# two cases:
"""if first element is less than middle,   
    either the first element is minimum, or the answer is in the second half
    if the last element is less than the last element, than the answer is in the second half
if first element is greater than the middle, 
    the anwer is either the middle element, or in the first half"""


def find_minimum(arr):
    if len(arr) == 0:
        raise ValueError('Function find_minimum cannot be passed empty array')
    if len(arr) == 1:
        return arr[0]
    
    index = math.floor(len(arr) / 2) 
    first = arr[0]
    
    if first < arr[index]:
        if first < arr[len(arr)-1]:
            return first    
        # throw away first half
        arr = arr[index:]
        return find_minimum(arr)
    else:
        if arr[index] < arr[index - 1]:
            return arr[index]
        arr = arr[:index+1]
        return find_minimum(arr)
        
# Quick Testing        
print(find_minimum(ex1))
print(find_minimum(ex2))    
print(find_minimum(ex3))
try:
    find_minimum([])
except ValueError as e:
    print(str(e))
except:
    print('caught unknown error')
else:
    print('expected error')
# questions to ask in an interview:    
# want me to return values or indicies?
# are all elements unique value?
# if there is one element, if empy list, if wrong value

# things to think about
# bsa: what if pivot element is smallest?
# what if array isnt rotated at all?