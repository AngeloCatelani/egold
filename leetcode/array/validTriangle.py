def triangleNumber( nums) -> int:
        output = 0
        n = len(nums)
        nums.sort()
        for k in range(0,n):


            i,j = 0,k-1
            while i < j:
                if nums[i]+nums[j] > nums[k]:
                    output += j-i
                    # j-=1
                else:
                    i+=1
        return output
        # time nlogn(n^2)
        # space O(1)
print(triangleNumber([2,2,3,4]))
print(triangleNumber([4,2,3,4]))