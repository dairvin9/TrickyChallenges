# Given an array of integers, assuming there are at least 3 integers, find the highest product of three of the integers
import functools

arr = [56, 23, 87, 12]
arr2 = [-56, 23, -87, -67, 45]

def getHighestProduct(arr):
	# i could sort the array
	# see if multiplying the two smallest is better than mulitplying the second and third largest
	largest = [0,0,0]
	smallest = [0,0]
	for item in arr:
		for num_index in range(1,len(largest)):
			if item > largest[num_index]:
				largest[num_index + 1:] = largest[num_index:len(largest) - num_index ]
				largest[num_index] = item
		for num_index in range(1,len(smallest)):
			if item < smallest[num_index]:
				smallest[num_index + 1:] = smallest[num_index:]
				smallest[num_index] = item
	if smallest[0] * smallest[1] > largest[1] * largest[2]:
		return functools.reduce(lambda x, y: x*y, smallest) * largest[0]
	else:
		return functools.reduce(lambda x,y: x*y, largest) 

print(getHighestProduct(arr))
print(getHighestProduct(arr2)) 

	
