class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        # clarification O/p boolean
        # test cases
        # Implement
        # verify

        # normal binary search
        # l = 0 
        # r= len(nums)-1
        # while l<=r:
        #     m = (l+r)//2
        #     if nums[m] == target:
        #         return true
        #     if nums[m] < target:
        #         # move the left
        #         l = m+1
        #     else:
        #          r = m-1
        # return false
        l = 0
        r = len(nums)-1
        while l <= r:
            m = (l+r)//2
            if nums[m] == target:
                return True
            if nums[l] == nums[m] == nums[r]:
                l += 1
                r -= 1
            elif nums[l] <= nums[m]:
                if nums[l] <=target < nums[m]:
                    r = m-1
                else:
                    l = m+1


            else:
                if nums[m] < target <= nums[r]:
                    l = m+1
                else:
                    r = m-1

        return False

        