def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
if not grid:
            return 0

        row = len(grid)
        column = len(grid[0])
        
        visited = set()
        maxA = 0

        def bfs(r,c):
            queue = []
            area = 0
            queue.append((r,c))
            visited.add((r,c))

            while queue:
                r1,c1 = queue.pop()
                area +=1
                # print(area)
                directions = [[0,1],[0,-1],[1,0],[-1,0]]
                for dr,dc in directions:
                    R = r1+dr
                    C = c1+dc
                    if R in range(row) and C in range(column) and grid[R][C] ==1 and (R,C) not in visited:
                        queue.append((R,C))
                        visited.add((R,C))
            return area    
            

       
        for r in range(row):
            for c in range(column):
                if grid[r][c] == 1 and (r,c) not in visited:
                   
                    maxA = max(maxA,bfs(r,c))
                    
                   
                    
        
        return maxA
grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
print(islandPerimeter(grid))



 if not grid:
            return 0
        row = len(grid)
        column = len(grid[0])
        maxA = 0
        visit = set()

        def dfs(r,c):
            if (r<0 or r==row or c<0 or c == column or grid[r][c] == 0 or (r,c) in visit): return 0
            else:
                visit.add((r,c))
                return (1+dfs(r-1,c)+dfs(r+1,c)+dfs(r,c-1)+dfs(r,c+1))


        for i in range(row):
            for j in range(column):
                if grid[i][j] == 1 or (i,j)not  in visit:
                    maxA = max(maxA,dfs(i,j))
        return maxA
