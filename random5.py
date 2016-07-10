# You have a function rand5() that generates a random integer from 1 to 5. Use it to write a function rand7() that generates a random integer from 1 to 7.

import random

# Magic given function
def rand5():
	return random.randint(1,5)

# My super cool function    
# It gives me one in 5. what if I do (5) * 7, which will give me a number 7 to 35. Divide this number by 5
def rand7():

    # So we dont have to recur
    while True:
        # Think of it graphically, we are gonna throw out the last four values
"""        
        board = [
            [1,2,3,4,5],
            [6,7,1,2,3],
            [4,5,6,7,1],
            [2,3,4,5,6],
            [7,1,2,3,4],
        ]
"""        
        
        
        xcor = rand5()
        ycor = rand5()

        
        number = (ycor - 1)* 5 + xcor 
        if number > 21:
            continue
        
        return number % 7 + 1   
        
    
def test():
    results = [0,0,0,0,0,0,0]
    for n in range(0,1000000):
        results[ rand7()-1 ] += 1
        
    print results    
        
test()        
    