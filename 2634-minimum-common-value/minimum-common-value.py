class Solution(object):
    def getCommon(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        # arr = []
        # for i in range(len(nums1)):
        #     if nums1[i] in nums2:
        #         arr.append(nums1[i])
        # return min(arr) if arr else -1
        # set_nums2 = set(nums2)  # Convert nums2 to a set for O(1) membership checking
        # common = []
        # for num in nums1:
        #     if num in set_nums2:
        #         common.append(num)
        # return min(common) if common else -1
        i, j = 0, 0
        
        # Use two pointers to traverse the arrays.
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                i += 1
            elif nums1[i] > nums2[j]:
                j += 1
            else:
                # Found a common element; it's the smallest one because arrays are sorted.
                return nums1[i]
                
        return -1