def orangesRotting(self, grid: List[List[int]]) -> int:
        #  dfs does not work because it works on one orange at a time so it increases the time to detect the rotten oranges
        #  but bfs works simultanesouly on rotten orange - multifunctional bfs

        row = len(grid)
        col = len(grid[0])
        time = 0
        fresh = 0
        queue = deque()
        directions = [[0,1],[0,-1],[1,0],[-1,0]]


        for r in range(row):
            for c in range(col):
                if grid[r][c] == 1:
                    fresh+=1
                if grid[r][c] == 2:
                    queue.append([r,c])
        

        while queue and fresh >0 :
            for i in range(len(queue)):
                r,c = queue.popleft()
                print(r,c)
                for dr,dc in directions:
                    r1 = dr+r
                    c1 = dc+c
                    if r1 <0 or r1 == row or c1< 0 or c1== col or grid[r1][c1] != 1:
                        continue
                    else:
                        grid[r1][c1] =2
                        queue.append([r1,c1])
                        fresh-=1
            time+=1
        return time if fresh ==0 else -1
# time - O(n*m)