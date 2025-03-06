def threeSum( nums):
        res = []
        l = 0
        r = len(nums)-1
        while l<r:
            if nums[l] + nums[r] + nums[r-1] == 0:
                res.append([nums[l],nums[r],nums[r-1]])
                r-=1
            if len(res) <= len(nums):
             return res
            else:
                r-=1
        
# print(threeSum([-1,0,1,2,-1,-4]))
print(threeSum([0,0,0]))