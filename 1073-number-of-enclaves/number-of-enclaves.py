class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        visit = set()

        def dfs(i,j):
            res = 1
            if i < 0 or j < 0  or i>= rows or j >= cols or (i,j) in visit or grid[i][j] == 0:
                return 0
            visit.add((i,j))
            res += dfs(i+1,j)
            res +=dfs(i-1,j)
            res +=dfs(i,j+1)
            res +=dfs(i,j-1)

            return res


        land,borderLand = 0,0
        for i in range(rows):
            for j in range(cols):
                land += grid[i][j]
                if grid[i][j] == 1 and (i,j) not in visit and (j in [0,cols-1] or  i in [0 , rows-1]):
                    borderLand +=dfs(i,j)
        return land - borderLand
        