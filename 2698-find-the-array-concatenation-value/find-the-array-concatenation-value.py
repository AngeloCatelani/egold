class Solution(object):
    def findTheArrayConcVal(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = 0
        r = len(nums) - 1
        output = 0

        # Process pairs from both ends
        while l < r:
            n1 = str(nums[l])
            n2 = str(nums[r])
            output += int(n1 + n2)
            l += 1
            r -= 1

        # If there's a middle element (odd-length array), add it once
        if l == r:
            output += nums[l]

        return output