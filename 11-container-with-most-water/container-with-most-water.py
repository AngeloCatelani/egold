class Solution:
    def maxArea(self, nums: List[int]) -> int:
        maxL = 0
        l=0
        r = len(nums)-1
        while l<r:
            area = r-l
            maxL = max(maxL,min(nums[l],nums[r])*area)
            if nums[l] <= nums[r]:
                l+=1
            else:
                r-=1
        return maxL