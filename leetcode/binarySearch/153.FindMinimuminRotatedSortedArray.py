def findMin( nums) :
        l = 0 
        r = len(nums)-1
        curmin = float("inf")
        while l<r:
            m = (l+r)//2
            curmin = min(curmin, nums[m])
            # if it is in right side
            if nums[m] > nums[r]:
                l = m+1
            else:
                r = m-1
        return min(curmin,nums[l]) 
print(findMin([3,4,5,1,2]))
print(findMin([4,5,6,7,0,1,2]))
            

