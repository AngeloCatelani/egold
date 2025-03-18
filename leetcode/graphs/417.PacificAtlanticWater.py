def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        res = []
        row = len(heights)
        column = len(heights[0])
        pac = set()
        atl = set()

        def dfs(r,c,visit,prevHeights):
            if(r<0 or r== row or c<0 or c== column or heights[r][c] < prevHeights or (r,c)in visit):
                return
            else:
                visit.add((r,c))
                dfs(r+1,c,visit,heights[r][c])
                dfs(r-1,c,visit,heights[r][c])
                dfs(r,c+1,visit,heights[r][c])
                dfs(r,c-1,visit,heights[r][c])      


        for c in range(column):
            #  rows(0)and col(0) is in pacific ocean
        # row-1 and col(0) is in atlatic ocean
            dfs(0,c,pac,heights[0][c])
            dfs(row-1,c,atl,heights[row-1][c])
        
        for r in range(row):
             dfs(r,0,pac,heights[r][0])
             dfs(r,column-1,atl,heights[r][column-1])
        
        for i in range(row):
            for j in range(column):
                if (i,j) in pac and (i,j) in atl:
                    res.append([i,j])
        return res
        
# time = O(n*m)

# bfs
# def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
#         # dfs

#         row = len(heights)
#         col = len(heights[0])
#         res =[]
#         pac = set()
#         atl = set()

#         def bfs(r,c,visit,prevHeights):
#             queue = []
#             queue.append((r,c))
#             while queue:
#                 r1,c1 = queue.pop()                       
#                 if (r1<0 or c1<0 or r1==row or c1 ==col or heights[r1][c1] < prevHeights or (r1,c1) in visit):return
#                 else:
#                     visit.add((r1,c1))
#                     queue.append((r1,c1))
#                     bfs(r1+1,c1,visit,heights[r1][c1])
#                     bfs(r1-1,c1,visit,heights[r1][c1])
#                     bfs(r1,c1+1,visit,heights[r1][c1])
#                     bfs(r1,c1-1,visit,heights[r1][c1])



#         for c in range(col):
#             bfs(0,c,pac,heights[0][c])
#             bfs(row-1,c,atl,heights[row-1][c])
#         for r in range(row):
#             bfs(r,0,pac,heights[r][0])
#             bfs(r,col-1,atl,heights[r][col-1])
        
#         for i in range(row):
#             for j in range(col):
#                 if (i,j) in pac and (i,j) in atl:
#                     res.append([i,j])
#         return res