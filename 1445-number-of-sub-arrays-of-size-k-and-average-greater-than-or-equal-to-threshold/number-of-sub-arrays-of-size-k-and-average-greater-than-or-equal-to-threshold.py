# class Solution:
#     def numOfSubarrays(self, nums: List[int], k: int, threshold: int) -> int:
#         if len(nums)<k:
#             return 0;
#         l = 0;
#         res = 0;
#         total = 0;
        
#         for r in range(nums[:k]):
            
#             total +=nums[r];
#             if total/k >= threshold:
#                 res += 1                   
#                 total -= nums[l]
#                 l+=1;
                
                
#         return res;
class Solution:
    def numOfSubarrays(self, nums: List[int], k: int, threshold: int) -> int:
        if len(nums) < k:
            return 0
        
        l = 0
        res = 0
        total = sum(nums[:k])  # Initial window sum
        
        # Check the first window
        if total / k >= threshold:
            res += 1
        
        # Slide the window
        for r in range(k, len(nums)):
            total += nums[r] - nums[l]
            l += 1
            if total / k >= threshold:
                res += 1
        
        return res



        