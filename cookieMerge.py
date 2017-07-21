"""
  We have our lists of orders sorted numerically already, in lists. Write a function to merge our lists of orders into one sorted list.
"""

my_list     = [3, 4, 6, 10, 11, 15]
alices_list = [1, 5, 8, 12, 14, 19]

def merge_lists(list1, list2):
    combined = [None] * (len(list1) + len(list2))
    index1 = 0
    index2 = 0
    for x in range(0,len(combined)):
        if len(list1) == index1:
            combined[x] = list2[index2]
            index2 +=1
        elif len(list2) == index2:
            combined[x] = list1[index1]
            index1 +=1    
        elif list1[index1] < list2[index2]:
            combined[x] = list1[index1]
            index1 +=1  
        else:
            combined[x] = list2[index2]
            index2 +=1
    return combined    
print (merge_lists(my_list, alices_list))