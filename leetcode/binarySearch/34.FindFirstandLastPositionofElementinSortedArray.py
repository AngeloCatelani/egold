def searchRange( nums, target):
        left = binsearch(nums,target,True)
        right =binsearch(nums,target,False)
        return [left,right]

def binsearch(nums,target,leftBias):
        l = 0
        r = len(nums)-1
        i = -1
        while l<=r:
            m = (l+r)//2
            if nums[m] < target:
                l = m+1
            elif nums[m] > target:
                r = m-1
            else:
                i = m
                if leftBias:
                    r = m-1
                else:
                    l = m+1
        return i
            
print(searchRange([5,7,7,8,8,10],8))    