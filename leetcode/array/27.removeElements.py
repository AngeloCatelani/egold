def removeElement( nums, val):
        # if element is equal to val remove it by del
        # for i in range(len(nums)):
        #     # print (i)
        #     if nums[i] == val:
        #         del nums[i]
        #         # nums.append('_')
        # return len(nums)
        #         # print(nums)
        count =0
        for i in range(len(nums)):
            if nums[i]== val:
                continue
            else:
                nums[count] = nums[i]
                print(nums[count])
                count+=1
        return count

# second solution
        for i in range(nums.count(val)): # loop runs times of val
        #     print(nums.count(val))
        #     # print (i)
            # if nums[i] == val:
            nums.remove(val)
               
                # nums.append('_')
        return len(nums)
            
print(removeElement([3,2,2,3],3))