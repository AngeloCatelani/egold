class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        map = {}

        for i in range(len(nums)):
            if nums[i] in map:
                map[nums[i]] +=1
            else:
                map[nums[i]] = 1
        count = 0
        k = 0
        for key,val in map.items():
            
            if val > count:
                count = val
                k = key
            else:
                continue
        return k
            