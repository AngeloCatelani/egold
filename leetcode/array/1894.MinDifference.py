def minimumDifference( nums, k) :
        visited = set()
        for i in range(len(nums)):
            for j in range(1,len(nums)):
                diff = abs(nums[i] - nums[j])
                visited.add(diff)
                print(visited)
        return min(visited,default=0)
print(minimumDifference([9,4,1,7],2))