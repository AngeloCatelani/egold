class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        s = set()
        l = 0
        for r in range(len(nums)):
            if r-l > k:
                s.remove(nums[l])
                l+=1
            if nums[r] in s:
                return True
            else:
                s.add(nums[r])
        return False
            



        

                
        