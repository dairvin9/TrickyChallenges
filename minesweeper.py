# Leetcode solution, unfortunately leetcode uses python 2.

adj = [-1, 0, 1]
labels = map(str,range(9))
labels[0] = 'B'

class Solution(object):
    
    @staticmethod
    def countAdjacentMines(board, x, y):
        mines = 0
        for (adj_x, adj_y) in [(x + i, y + j) for i in adj for j in adj if i != 0 or j != 0]:
            if adj_x < 0 or adj_y < 0 or adj_x > len(board[0]) - 1 or adj_y > len(board) - 1:
                continue
            if board[adj_y][adj_x] == 'M':
                mines += 1
        return mines  
    
    def floodfill(self, board, x, y):
        # set the tile to its number of adjacent
        # if B, recurse
        
        numAdj = Solution.countAdjacentMines(board, x, y)
        board[y][x] = labels[numAdj]
        
        if board[y][x] == 'B':
            for (adj_x, adj_y) in [(x + i, y + j) for i in adj for j in adj if i != 0 or j != 0]:
                if adj_x < 0 or adj_y < 0 or adj_x > len(board[0]) - 1 or adj_y > len(board) - 1:
                    continue
                if board[adj_y][adj_x] == 'E':
                    self.floodfill(board, adj_x, adj_y)


    def updateBoard(self, board, click):
        """
        :type board: List[List[str]]
        :type click: List[int]
        :rtype: List[List[str]]
        """
        # cases:
        # M -> turn to x and return
        # E -> if no mines -> flood fill
        # E -> if mines -> put number and return
        
        for index in range(len(board)):
            board[index] = list(board[index])
        
        x = click[1]
        y = click[0]
        
        if board[y][x] == 'M':
            board[y][x] = 'X'
            
        else:
            self.floodfill(board, x, y)
        
        return board
        
        # optimizing for multiple queries? Could build a board with adjacencies calculated in (probalby not useful tho)
        
