class Solution:
    def maxProfit(self, nums: List[int]) -> int:
        maxL = 0
        l = 0
        for r in range(1,len(nums)):
            if nums[l] < nums[r]:
                profit = nums[r]- nums[l]
                maxL = max(maxL,profit)
            else:
                l = r
        return maxL
