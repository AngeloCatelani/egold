def productExceptSelf( nums) :
        res =[1]*len(nums) #[1,1,1,1]
        prefix =1
        for i in range(len(nums)): #going forward
            res[i] *= prefix
            prefix *= nums[i] 
            # res[1, 1, 2, 6]
        postfix =1
        for i in range(len(nums)-1,-1,-1): # going backwards (range -> start,stop,step)
            res[i] *= postfix  # postfix gets its value from nums array
            postfix *=nums[i] 
        return res

        # time =O(n)
        # space = O(1)
print(productExceptSelf([1,2,3,4]))

        # res = [1]*len(nums)
        # prefix =1
        # for i in range(len(nums)):
        #     res[i] = res[i]*prefix
        #     prefix = prefix *nums[i]
        # postfix =1
        # for i in range(len(nums)-1 ,-1,-1):
        #      res [i] = res[i]*postfix
        #      postfix = postfix * nums[i]
        # return res
        # # time =O(n)
        # # space = O(1)
