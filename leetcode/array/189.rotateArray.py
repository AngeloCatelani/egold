def rotate( nums, k):
        """
        Do not return anything, modify nums in-place instead.
        """
        # k = k % len(nums) used when 

        # i = 0
        # while i < k:
        #     temp = nums.pop()
        #     nums.insert(0, temp)
        #     i += 1
        
        # from collections import deque
        # k = k % len(nums)
        # i = 0
        # d = deque(nums)
        # while i < k:
        #     temp = d.pop()
        #     d.appendleft(temp)
        #     i += 1
        # print(nums[:])
        # nums[:] = d #Assigning it to nums[:] stuffs it into the existing list,nums[:]
        # print(nums[:])

        k = k%len(nums)
        i = 0
        d =deque(nums)
        while i  < k:
            pop = d.pop()
            d.appendleft(pop)
            i+=1
        nums[:] = d

        
print(rotate([1,2,3,4,5,6],11))