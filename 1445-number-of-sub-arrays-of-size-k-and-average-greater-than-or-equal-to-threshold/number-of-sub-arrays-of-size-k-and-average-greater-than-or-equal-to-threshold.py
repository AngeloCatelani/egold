class Solution:
    def numOfSubarrays(self, nums: List[int], k: int, threshold: int) -> int:
        if len(nums)<k:
            return 0;
        
        res = 0;
        total = sum(nums[:k-1]);
        
        for r in range(len(nums)-k+1):            
            total +=nums[r+k-1];
            if total/k >= threshold:
                res += 1                   
            total -= nums[r]        
           
                
        return res;
# def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
#         res = 0
#         curSum = sum(arr[:k-1])

#         for L in range(len(arr) - k + 1):
#             curSum += arr[L + k - 1]
#             if (curSum / k) >= threshold:
#                 res += 1
#             curSum -= arr[L]
#         return res