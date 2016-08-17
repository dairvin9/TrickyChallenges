"""Write a function for finding the index of the "rotation point," which is where I started working from the beginning of the dictionary. This list is huge (there are lots of words I don't know) so we want to be efficient here

So we are given a list, that is in alphabetical order, but started somewhere random in the alphabet and wrapped around. Like ['know', 'man','wears','bandanas','duh']. I need to find the index of the first alphabetical point of the list. I bet I can do it in less than O(n)"""

# I am going to put everything in lowercase for good measure.

def find_rotator_point(word_list):
	first_char = word_list[0][0]
	
	end_index = len(word_list)-1
	beg_index = 0
	
	if word_list[end_index] > word_list[beg_index]:
		return beg_index
	while True: 
		if end_index-beg_index == 0:
			return beg_index
		
		half = (end_index-beg_index)//2 + beg_index
		
		if word_list[half] >= first_char: # check out second half of list
			beg_index = half+1
		else: # checkout first half of list
			end_index = half
		#print (beg_index,end_index,half)	
		
print (find_rotator_point(['know', 'man','wears','bandanas','duh']))
print (find_rotator_point(['know', 'man','wears','bandanas']))
print (find_rotator_point(['know', 'man','wears','bandanas','duh','embers']))
print (find_rotator_point(['know', 'man','wears']))