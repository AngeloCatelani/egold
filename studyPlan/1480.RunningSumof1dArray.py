def runningSum(self, nums: List[int]) -> List[int]:
        output =[]
        j=0
        sum =0
        for i in range(1,len(nums)+1):
            if j==i:
                j=0
            sum+=nums[j]
            j+=1
            output.append(sum)
        return output
