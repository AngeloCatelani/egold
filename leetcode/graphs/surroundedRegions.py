def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        # if 0 in border convert to T
        # if O not in border convert to "X"
        #  convert T to back O

        row = len(board)
        col = len(board[0])

        def dfs(r,c):
            if (r<0 or c<0 or r== row or c== col or board[r][c] != "O"):
                return
            else:
                board[r][c] = "T"
                dfs(r+1,c)
                dfs(r-1,c)
                dfs(r,c+1)
                dfs(r,c-1)
        for i in range(row):
            for j in range(col):
                if board[i][j] == "O" and ((i in [0,row-1])or ( j in [0,col-1]) ):
                    dfs(i,j)
        

        for i in range(row):
            for j in range(col):
                if board[i][j] == "O":
                    board[i][j] = "X"
        

        for i in range(row):
            for j in range(col):
                if board[i][j] == "T":
                    board[i][j] = "O"
        
# time O(n*m)
