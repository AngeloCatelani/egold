class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        countS = set()
        
        for r in range(len(nums)):
            if nums[r] in countS:
                return nums[r]
            else:
                countS.add(nums[r])
        return -1