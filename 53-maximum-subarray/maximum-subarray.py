class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxL = nums[0]
        currS = 0
        for s in nums:
            currS += s
            maxL = max(maxL,currS)
            if currS <0:
                currS = 0
        return maxL