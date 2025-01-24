def pivotIndex( nums) :
    leftSum = 0
    totalSum = 0
    for i in range(len(nums)):
        totalSum +=nums[i]
    for i in range(len(nums)):
        rightSum = totalSum - nums[i] - leftSum
        if rightSum == leftSum:
            return i
        else:
            leftSum +=nums[i]
    return -1
print(pivotIndex( [1,7,3,6,5,6]))
print(pivotIndex( [1,7,3,6,5,6,10,6,3,5,6]))
    
