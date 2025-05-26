def getConcatenation(self, nums: List[int]) -> List[int]:
        # print(2*nums)
        # return 2*nums
        ans = []
        for i in range(2): # will run loop 2 times
            for n in nums:
                ans.append(n)
        return ans