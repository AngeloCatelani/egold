class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows = len(board)
        cols = len(board[0])

        for i in range(rows):
            for j in range(cols):
                liveCells =-board[i][j]
                for x in range(i-1,i+2):
                    for y in range(j-1,j+2):
                        if 0<=x<rows and 0<=y<cols and board[x][y] >0:
                            liveCells +=1
                if board[i][j] and (liveCells <2 or liveCells >3):
                    board[i][j]=2
                if board[i][j] == 0 and liveCells == 3:
                    board[i][j]= -1



        for i in range(rows):
            for j in range(cols):
                if board[i][j] == 2:
                    board[i][j]=0
                if board[i][j] == -1:
                    board[i][j]= 1