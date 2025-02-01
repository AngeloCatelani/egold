def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # same binary search concept but have a matrix.
        # use for loop to get each row
        for i in range(len(matrix)):
            # print(matrix[i])
            l = 0
            r = len(matrix[i])-1
            while l<=r:
                m = (l+r)//2
                print(matrix[i][m])
                if matrix[i][m] == target:
                    return True
                elif matrix[i][m] < target:
                    l = m+1
                elif matrix[i][m] > target:
                    r = m-1
        return False
