
def missingNumber(nums) -> int:
    i=0
    while i <= len(nums):
    #   for i in range(len(nums)):
          if i not in nums:
              return i
          i=i+1
   
    #   res = len(nums)
    #   for i in range(len(nums)):
    #       res += (i - nums[i])
    #   return res
print(missingNumber([3,0,1]))
print(missingNumber([0,1]))
       