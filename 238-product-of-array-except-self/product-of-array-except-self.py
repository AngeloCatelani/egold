class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        post = 1
        pre =1
        for i in range(len(nums)):
            res[i] = res[i] * pre
            pre = pre * nums[i]
        
        for i in range(len(nums)-1,-1,-1):
            res[i] = res[i] * post
            post = post * nums[i]
        return res