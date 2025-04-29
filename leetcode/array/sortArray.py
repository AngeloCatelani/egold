def sortArray(nums) :
        j=0
        output = []
        for n in nums:
            if nums[j] < n:
                output.append(nums[j])
            # else:
            #     j+=1
        return output
print(sortArray([5,2,3,1]))