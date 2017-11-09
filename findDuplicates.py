# optimizing for space
def findDuplicates(arr):
	arr.sort() # destroy input
	prev = None 
	for num in arr:
		if num == prev:
			return num
		prev = num

	raise ValueError("List has no duplicates!")

#no destroy input
def findDuplicatesBetter(arr):
	beg = 1
	end = len(arr) - 1
	while beg < end:

		num_elements_in_first_half = 0
		for num in arr:
			half = (beg + end) // 2 # rounds down
			if num >= beg and num <= half:
				num_elements_in_first_half += 1

		if num_elements_in_first_half > (len(arr) - num_elements_in_first_half):
			end = half
		else:
			beg = half + 1

	return beg

	raise ValueError("List has no duplicates!")

#cant assume sorted. 
test1 = [1,2,2,2,4]
test2 = [1,2,2]
test3 = [3,2,1,3]

print(findDuplicatesBetter(test1) == 2)
print(findDuplicatesBetter(test2) == 2)
print(findDuplicatesBetter(test3) == 3)


