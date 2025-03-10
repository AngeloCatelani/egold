def islandPerimeter(grid) :
        # use set to have visited cells
        # have a helper func dfs to go depth depth
        # conditions to check i>=len(grid) or j>=len(grid[0]) or i<0 or j<0
        #  grid[i][j] == 0 : return 1
        #  if i,j in visited set return 0

        visit = set()
        def dfs(i,j):
            if i>=len(grid) or j>=len(grid[0]) or i<0 or j<0 or grid[i][j] == 0 :
                return 1
            if (i,j) in visit:
                return 0
            
            visit.add((i,j))

            perim = dfs(i,j+1)
            perim += dfs(i+1,j)
            perim += dfs(i-1,j)
            perim += dfs(i,j-1)

            return perim
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]:
                    return dfs(i,j)
    # time = O(n*m)
    # space = O(n*m)
    
        