class Solution(object):
    
    def distinctAverages(self, nums, s=None):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()  # O(n log n)
        left, right = 0, len(nums) - 1
        avg_set = set()
        
        while left < right:  # O(n)
            avg = (nums[left] + nums[right]) / 2.0
            avg_set.add(avg)
            left += 1
            right -= 1
        
        return len(avg_set)  # Number of unique averages

# Time Complexity Analysis
# Sorting (O(n log n))
# Two-Pointer Iteration (O(n))
# Adding to Set (O(1) per operation, total O(n))
# Final time complexity: O(n log n) + O(n) = O(n log n).

# Space Complexity Analysis
# Set stores at most n/2 unique values (O(n)), but since we don’t use extra data structures beyond a few variables, it's O(n) in the worst case.
# However, if we consider only extra space apart from input, it's O(1).
# Final space complexity: O(n) worst case, but O(1) auxiliary space.