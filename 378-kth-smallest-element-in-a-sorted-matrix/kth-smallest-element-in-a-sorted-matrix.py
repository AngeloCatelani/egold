class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        low = matrix[0][0]
        high = matrix[n - 1][n - 1]
        
        while low <= high:
            mid = low + (high - low) // 2
            count = self.getLowerNum(matrix, mid)
            if count < k:
                low = mid + 1
            else:
                high = mid - 1
        
        return low
    
    def getLowerNum(self, matrix: List[List[int]], num: int) -> int:
        n = len(matrix)
        row = n - 1
        col = 0
        res = 0
        
        while row >= 0 and col < n:
            if matrix[row][col] > num:
                row -= 1
            else:
                res += row + 1
                col += 1
        
        return res