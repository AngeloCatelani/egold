class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        freshOrange = 0
        minPassed = 0
        visit =set()
        q = deque()
        def bfs(i,j):
            nonlocal freshOrange
            if i < 0 or j<0 or i>= rows or j>= cols or (i,j)in visit or grid[i][j] == 0:
                return
            visit.add((i,j))
            q.append((i,j))
            if grid[i][j] ==1:
                freshOrange -=1
                grid[i][j] = 2




        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    visit.add((i,j))
                    q.append((i,j))
                if grid[i][j] ==1:
                    freshOrange +=1
        while q and freshOrange >0:
            minPassed +=1
            for i in range(len(q)):
                r,c = q.popleft()
                bfs(r+1,c)
                bfs(r-1,c)
                bfs(r,c+1)
                bfs(r,c-1)
        return minPassed if freshOrange ==0 else  -1