class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        count = 0
        maxL = 0
        rows = len(grid)
        cols = len(grid[0])
        v = set()

        def dfs(i,j):
            if i<0 or i>= rows or j <0 or j>= cols or grid[i][j] == 0 or (i,j) in v:
                return 0
            v.add((i,j))
            area =1
            area += dfs(i+1,j)
            area += dfs(i-1,j)
            area += dfs(i,j+1)
            area += dfs(i,j-1)

            return area


        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1 and (i,j) not in v:
                    count = dfs(i,j)
                    maxL = max(maxL,count)
        return maxL