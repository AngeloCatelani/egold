class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0  # Edge case: empty list

        l = 0  # Pointer for the last unique element
        for r in range(1, len(nums)):
            if nums[r] != nums[l]:  # Found a unique element
                l += 1  # Move the unique position pointer
                nums[l] = nums[r]  # Place the unique element

        return l + 1  # Number of unique elements

