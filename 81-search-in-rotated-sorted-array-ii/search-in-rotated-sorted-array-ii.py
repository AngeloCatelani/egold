class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        l = 0
        r = len(nums)-1
        while l<=r:
            m = (l+r)//2
            if nums[m] == target:
                return True
             # Handling the case where we cannot be sure about the sorted part
            if nums[l] == nums[m] == nums[r]:
                l += 1
                r -= 1
            elif nums[l] <= nums[m]:  # Left part is sorted
                if nums[l] <= target < nums[m]:
                    r = m - 1
                else:
                    l = m + 1
            else:  # Right part is sorted
                if nums[m] < target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1
        return False