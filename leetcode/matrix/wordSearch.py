def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS = len(board)
        COLUMNS = len(board[0])

        path = set()

        def dfs(r , c , i):
            if i == len(word):
                return True
            if(r < 0 or c < 0 or r >=ROWS or c >= COLUMNS or word[i] !=board[r][c] or (r,c) in path):
                return False
            path.add((r,c))

            res = (dfs(r+1,c,i+1) or
            dfs(r-1,c,i+1) or
            dfs(r,c+1,i+1) or
            dfs(r,c-1,i+1))

            path.remove((r,c))
            return res
     
        for i in range(ROWS):
            for j in range(COLUMNS):
                if dfs(i,j,0):
                    return True
        return False


        # time O(n*m* 4^n)

