from typing import List
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        maxL = 0
        visited = set()
        count = 0
        def dfs(i,j):
            if i<0 or j <0 or i>= row or j >=col or grid[i][j] == 0:
                return 0
            if (i,j) in visited:
                return 0
            visited.add((i,j))
            area = 1
            area += dfs(i + 1, j)
            area += dfs(i - 1, j)
            area += dfs(i, j + 1)
            area += dfs(i, j - 1)
            return area



        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1 and (i,j) not in visited :
                    count = dfs(i,j)
                    maxL = max(maxL, count)
        return maxL

# from typing import List

# class Solution:
#     def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
#         row = len(grid)
#         col = len(grid[0])
#         maxL = 0
#         visited = set()
        
#         def dfs(i, j):
#             if i < 0 or j < 0 or i >= row or j >= col or grid[i][j] == 0:
#                 return 0
#             if (i, j) in visited:
#                 return 0
#             visited.add((i, j))
#             # Calculate area by visiting all connected cells
#             area = 1
#             area += dfs(i + 1, j)
#             area += dfs(i - 1, j)
#             area += dfs(i, j + 1)
#             area += dfs(i, j - 1)
#             return area

#         for i in range(row):
#             for j in range(col):
#                 if grid[i][j] == 1 and (i, j) not in visited:
#                     count = dfs(i, j)
#                     maxL = max(maxL, count)
#         return maxL