class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        freshOranges = 0
        minPassed = 0
        v = set()
        q = deque()
        def bfs(r,c):
            nonlocal freshOranges
            if r <0 or c < 0 or r>=rows or c>=cols or (r,c) in v or grid[r][c] == 0:
                return
            v.add((r,c))
            q.append((r,c))
            if grid[r][c] == 1:
                freshOranges -=1
                grid[r][c] = 2
            
            


        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    v.add((i,j))
                    q.append((i,j))
                if grid[i][j]==1:
                    freshOranges +=1

        while q and freshOranges >0:
            minPassed +=1
            for i in range(len(q)):
                r,c = q.popleft()
                
                bfs(r+1,c)
                bfs(r-1,c)
                bfs(r,c+1)
                bfs(r,c-1)
           

        return minPassed if freshOranges == 0 else -1