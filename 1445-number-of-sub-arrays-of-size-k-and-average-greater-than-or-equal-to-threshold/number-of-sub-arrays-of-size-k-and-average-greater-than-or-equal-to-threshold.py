class Solution:
    def numOfSubarrays(self, nums: List[int], k: int, threshold: int) -> int:
        count = 0
       
        l =0
        res = sum(nums[:k])
        if res / k >= threshold:
            count +=1
        for r in range(k,len(nums)):
            res += nums[r] - nums[l]
            l+=1
            if res / k >= threshold:
                count +=1 
        return count



