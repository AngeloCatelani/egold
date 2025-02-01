def searchInsert( nums, target) :
        # l = 0
        # r = len(nums)
        # # print(l,"l",r,"r")
        # while l<=r:
        #     m = l+(r-l)//2
        #     # print(m,"m",l,"l",r,"r")
            
        #     if nums[m] < target :
        #         l = m+1
        #     else  :
        #         r = m - 1
        # return l
        l = 0
        r = len(nums) - 1
        # print(l,"l",r,"r")
        while l<=r:
            # m = l+(r-l)//2
            m = (l+r)//2
            # print(m,"m",l,"l",r,"r")
            
            if nums[m] < target :
                l = m+1
            else  :
                r = m - 1
        return l
# print(searchInsert([1,3,5,6],2))
print(searchInsert([1,3,5,6,9,56],0))