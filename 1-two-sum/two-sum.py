class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i,n in enumerate(nums):
            diff =  target-n
            # print(diff)
            if diff in hashmap:
                # print(hashmap[diff],i)
                return [hashmap[diff],i]
            hashmap[n] = i
        