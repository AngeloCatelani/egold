class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def bs(nums):
            l = 0
            r = len(nums)-1
            while l <= r:
                m = (l+r)//2
                if nums[m] == target:
                    print(nums[m])
                    return True
                if nums[m] < target:
                    l = m+1
                else:
                    r = m-1
            return False
        
        for e in matrix:
            if bs(e):
                return True
        return False



        