class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
    
        # Initialize the search space
        left, right = 0, len(nums) - 1
      
        # Perform binary search to find the non-duplicate integer
        while left < right:
            # Calculate the middle index of the current search space
            mid = (left + right) // 2

            # Check if the middle element's value is equal to the next
            # or the previous based on whether mid is odd or even
            # Using XOR operation. If mid is even, mid ^ 1 will be mid + 1,
            # and if mid is odd, mid ^ 1 will be mid - 1.
            if nums[mid] != nums[mid ^ 1]:
                # If they are not equal, move the right pointer to mid.
                # We do this because the single element must be in the
                # first half if the pair is not complete in the mid.
                right = mid
            else:
                # If they are equal, this means the single element is in the
                # second half of the array. Move the left pointer to mid + 1.
                left = mid + 1
      
        # When left == right, the search space has been narrowed down to one element.
        # This remaining element is the non-duplicate integer we're looking for.
        return nums[left]