def minStartValue( nums) -> int:
    result = 0
    temp = 0
    for i in range(len(nums)):
        temp = temp + nums[i]
        result = min (result,temp)
    return abs(result)+1  # abs removes negative sign and makes it positive

print(minStartValue([-3,2,-3,4,2]))