# if there is a zero element in an mxn matrix, set the whole row and column to 0

ex = [[1, 1, 1, 0], [1, 1, 1, 1],[0, 1, 1, 1]]
# 1 0 1 0
# 1 1 1 1 
# 0 1 1 1

def setMNtoZeroIfZero(matrix):
	cols = [False] * len(matrix[0])
	rows = [False] * len(matrix)
	
	for i in range(len(rows)):
		for j in range(len(cols)):
			if matrix[i][j] == 0:
				cols[j] = True
				rows[i] = True
				
	for i in range(len(rows)):
		for j in range(len(cols)):
			if cols[j] == True or rows[i] == True:
				matrix[i][j] = 0
	return matrix
    
 
print(setMNtoZeroIfZero(ex))