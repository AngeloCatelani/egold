class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0;
        res = 0;
        minR = float('inf')
        for r in range(len(nums)):
            res +=nums[r];
            while res >= target:
                # a.append(nums[r])
                minR = min(r-l+1,minR)
                res -= nums[l];
                l+=1;
        return minR if minR != float('inf') else 0
            
        