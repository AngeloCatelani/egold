class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        l = 0
        target = sum(nums) - x
        currSum = 0
        windowSize = -1
        for r in range(len(nums)):
            currSum += nums[r]
            while currSum > target and l <= r:
                currSum -= nums[l]
                l += 1
            
            if currSum == target:
                windowSize = max(windowSize, r - l + 1)
                
        return -1 if windowSize == -1 else len(nums) - windowSize



        