# class Solution:
#     def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # rows = len(grid)
        # cols = len(grid[0])

        # visit = set()
        # maxL = 0
        # def dfs(i,j):
        #     if i < 0 or j<0 or i >= rows or j>= cols or (i,j) in visit or grid[i][j] == 0:
        #         return
        #     visit.add((i,j))
        #     area =1
        #     area += dfs(i,j+1)
        #     area += dfs(i,j-1)
        #     area += dfs(i+1,j)
        #     area += dfs(i-1,j)

        #     return area


        # for i in range(rows):
        #     for j in range(cols):
        #         if grid[i][j] == 1 and (i,j) not in visit:
        #             maxL = max(maxL ,dfs(i,j))
        # return maxL
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        visit = set()
        maxL = 0

        def dfs(i, j):
            if i < 0 or j < 0 or i >= rows or j >= cols or (i, j) in visit or grid[i][j] == 0:
                return 0  # Return 0 in the base case
            visit.add((i, j))
            area = 1  # Initial area for the current cell
            area += dfs(i, j + 1)
            area += dfs(i, j - 1)
            area += dfs(i + 1, j)
            area += dfs(i - 1, j)

            return area  # Return the accumulated area

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1 and (i, j) not in visit:
                    maxL = max(maxL, dfs(i, j))
        
        return maxL
