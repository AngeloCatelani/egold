def rotate( nums, k):
        """
        Do not return anything, modify nums in-place instead.
        """
        count =0
        for n in range(len(nums),-1,-1):
           
            if count != k:

                popped = nums.pop()
                nums.insert(0,popped)
                # print(nums)
                count+=1
        return nums
print(rotate([1,2,3,4,5,6],11))