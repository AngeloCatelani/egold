class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        dup = set()
        l = 0;
        for r in range(len(nums)):
            if r-l > k:
                dup.remove(nums[l])
                l+=1
            if nums[r] in dup:
                return True
            dup.add(nums[r])
        return False