class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()

        l = 0
        r = k-1
        minL = float("inf")
        while r < len(nums):
            minL = min(minL, abs(nums[l] - nums[r]))
            l+=1
            r+=1
        return minL


            

        