class Solution(object):
    
    def distinctAverages(self, nums, s=None):
        """
        :type nums: List[int]
        :rtype: int
        """
        if s is None:
            s = set()  # Initialize a set to store unique averages
        
        if not nums:  # Base case: stop when the list is empty
            return len(s)
        
        # Find and remove min/max correctly
        minNum = min(nums)
        maxNum = max(nums)
        nums.remove(minNum)
        nums.remove(maxNum)
        
        # Compute the average and store it in the set
        avg = (minNum + maxNum) / 2.0  # Keep as float to maintain precision
        s.add(avg)

        # Recursive call with the updated list and set
        return self.distinctAverages(nums, s)

    #  time =O(n)^2
    # space O(n)

