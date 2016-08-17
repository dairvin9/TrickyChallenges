"""Write a function fib() that a takes an integer n and returns the nth fibonacci number. In O(n)"""

def fib(n):
	if n < 0:
		raise ValueError
	if n == 0 or n==1:
		return n
	count = 1
	index_minus_two = 0
	index_minus_one = 1
	while count != n:
		temp = index_minus_one
		index_minus_one = index_minus_two + index_minus_one
		index_minus_two = temp
		
		count += 1
	return index_minus_two

print (fib(0))
print (fib(1))		
print (fib(2))		
print (fib(3))		
print (fib(4))		
print (fib(5))		
print (fib(6))		