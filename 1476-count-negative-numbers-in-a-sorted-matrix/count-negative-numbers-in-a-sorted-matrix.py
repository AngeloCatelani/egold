class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        count =0
        for i in range(len(grid)):
            count += self.binarysearch(grid[i],count)
        return count
    def binarysearch(self,grid:List[int],c):
        l = 0
        r = len(grid)-1
        while l <= r:
            m = (l+r)//2
            if grid[m] < 0:
                r = m - 1  # negatives are to the left
            else:
                l = m + 1  # negatives are to the right
        # 'l' ends up being the first index where row[l] < 0
        return len(grid) - l
