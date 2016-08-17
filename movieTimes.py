"""
Write a function that takes an integer flight_length (in minutes) and a list of integers movie_lengths (in minutes) and returns a boolean indicating whether there are two numbers in movie_lengths whose sum equals flight_length.
"""
def isExactLength(flight_length, movie_lengths):
	length_dict = {}
	for num in movie_lengths:
		if flight_length-num in length_dict:
			return True
		length_dict[num] = True
	return False
	
print (isExactLength(100,[2,56,2456,74,34,23,76])) # Supposed to fail
print (isExactLength(100,[2,56,2456,74,34,50,76])) # Supposed to fail (testing that it doesnt count 50 twice)
print (isExactLength(100,[2,56,2456,74,34,26,76])) # Supposed to succeed


# This is the solution with a set instead of a dictionary, because it is slightly better and I always forget the syntax for python sets.
def isExactLengthSet(flight_length, movie_lengths):
	length_set = set()
	for num in movie_lengths:
		if flight_length-num in length_set:
			return True
		length_set.add(num)
	return False
	
print (isExactLengthSet(100,[2,56,2456,74,34,23,76])) # Supposed to fail
print (isExactLengthSet(100,[2,56,2456,74,34,50,76])) # Supposed to fail (testing that it doesnt count 50 twice)
print (isExactLengthSet(100,[2,56,2456,74,34,26,76])) # Supposed to succeed