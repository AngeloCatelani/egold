def findDisappearedNumbers(nums):
        # output =[]
        # for i,n in enumerate(nums):
        #     print(i+1,"i")
        #     if i+1 not in nums:
        #         print(output)
        #         output.append(i+1)
        #         print(output,"2")
        #     else:
        #         continue
        # return output
        for n in nums:
            i = abs(n) - 1
            nums[i] = -1 * abs(nums[i])

        res = []
        for i, n in enumerate(nums):
            if n > 0:
                res.append(i + 1)
        return res
print(findDisappearedNumbers([4,3,2,7,8,2,3,1]))