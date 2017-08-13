# 1234
# 5678
# 9abc
# defg
import math

pic = [[1,2,3],[4,5,6],[7,8,9]]	
print(pic)


def rotate(square):
    num_rotations = math.floor(len(square)/2)
    len_square = len(square)
    
    for rotation in range(num_rotations):    
    # index should be number of swaps
        for index in range(0,len_square - 2*rotation - 1):
             
            square[rotation + index][rotation], square[len_square - rotation - 1][rotation + index], square[len_square - rotation - index - 1][len_square - rotation - 1], square[rotation][len_square - rotation - index - 1] = square[len_square - rotation - 1][rotation + index], square[len_square - rotation - index - 1][len_square - rotation - 1], square[rotation][len_square - rotation - index - 1], square[rotation + index][rotation] 
        return square        
def ifZeroSetZero(pic):
    pass            

    
print(rotate(pic))        
 