class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        #  i goes till len(m)-1
        #  j goes till len(n)-1
        # visited = set() to add the already visited boxes

        # will have two loop to go over the m*n
        # if (i,j) not in visited:
        # call dfs(i,j)
        
        # if the i goes below 0 or j < 0 or j>=n or i>=m or (i,j) is already in visited: return
        #  else: then add it to the viisted set and do dfs for neighbors(i+1,0)(0,j+1)
        # increment the count
        #  if it reaches last boz like [m][n] return count
        row = [1] * n
        for i in range(m-1):
            newRow = [1]*n
            for j in range(n-2,-1,-1):
                newRow[j] = newRow[j+1]+row[j]
            row = newRow
        return row[0]
       
        # O(n * m) O(n)







        