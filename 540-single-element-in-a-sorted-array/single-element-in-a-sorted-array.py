class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        # Initialize the pointers for binary search
        l, r = 0, len(nums) - 1
        
        # Binary search
        while l < r:
            mid = (l + r) // 2
            
            # Ensure mid is even to compare pairs correctly
            if mid % 2 == 1:
                mid -= 1
            
            # Check if the pair mid and mid + 1 is equal
            if nums[mid] == nums[mid + 1]:
                # If they are equal, the single element must be on the right side
                l = mid + 2
            else:
                # If they are not equal, the single element must be on the left side or at mid
                r = mid
        
        # l will eventually point to the single element
        return nums[l]