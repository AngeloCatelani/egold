class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums)-1
        curr = float("inf")
        while l <=r:
            m = (l+r)//2
            curr = min(curr,nums[m])
            if nums[m] > nums[r]:
                l = m+1
            else:
                r = m-1
        return min(curr,nums[l])
            