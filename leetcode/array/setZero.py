def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
  
        rowMap = set()
        colMap = set()
        row = len(matrix)
        col = len(matrix[0])
        for i in range(row):
            for j in range(col):
                if matrix[i][j] == 0:
                    rowMap.add((i))
                    colMap.add((j))


        for i in range(row):
            for j in range(col):
                if (i) in rowMap or (j) in colMap:
                    matrix[i][j] =0
        return matrix