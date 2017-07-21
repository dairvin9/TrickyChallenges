# 1234
# 5678
# 9abc
# defg
pic = [[1,2,3],[4,5,6],[7,8,9],['a','b','c']]	
print(pic)

def multiswap(a,b,c,d):
    d,a,b,c = a,b,c,d
    return a,b,c,d


def rotate():
    num_rotations = round(len(pic)/2)
    num_to_swap = len(pic) - 1
    
    for x in range(0,num_rotations):
        multiswap(pic[0][0],pic[3][0],pic[3][3],pic[0][3])

def ifZeroSetZero(pic):
                
print(pic)        
 