import collections
def numIslands( grid):
        # if grid is empty return 0
        #  row = len(grid) column = len(grid[0])
        # island = 0
        if not grid:
            return 0
        row = len(grid)
        column = len(grid[0])
        island =0
        visited = set()

        def bfs(r,c):
            queue = collections.deque()
            visited.add((r,c))
            queue.append((r,c))

            while queue:
                r , c  = queue.popleft() # breadthfirst
                # if they ask to depthfirst search do just pop() it will remove it from right
                directions = [[1,0],[-1,0],[0,1],[0,-1]]
                for dr,dc in directions:
                    rowDr = r+dr
                    columnDc = c+dc
                    if((rowDr in range(row) and  columnDc in range(column) and grid[rowDr][columnDc] =="1" and(rowDr,columnDc) not in visited)):
                        visited.add((rowDr,columnDc))
                        queue.append((rowDr,columnDc))



        for r in range(row):
            for c in range(column):
                if grid[r][c] == "1" and (r,c )not in visited:
                    bfs(r,c)
                    island +=1
        return island
grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
print(numIslands(grid))