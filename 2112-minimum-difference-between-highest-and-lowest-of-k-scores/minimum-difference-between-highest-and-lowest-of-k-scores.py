class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        minL = float("inf")
        l = 0
        r = k-1

        while r < len(nums):
             minL = min(minL,abs(nums[l] - nums[r]))
             l+=1
             r+=1
        return minL
       
            

        