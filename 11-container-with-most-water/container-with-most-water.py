class Solution:
    def maxArea(self, nums: List[int]) -> int:
        l = 0
        r = len(nums)-1
        maxL = 0
        while l < r:
            maxL = max(maxL , min(nums[l] , nums[r])* (r-l))
            if nums[l] < nums[r]:
                l+=1
            elif nums[r] <= nums[l]:
                r -=1
        return maxL
        