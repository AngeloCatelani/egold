def twoSum( nums, target ) :
    hashmap = {}
    for i, n in enumerate(nums):
        diffs = target-n
        if diffs in hashmap:
            return [hashmap[diffs],i]
        hashmap[n] = i
    return
print(twoSum([2,7,11,15],9))
    # time and space-O(n)

    #    def twoSum(self, nums: List[int], target: int) -> List[int]:
    #     hashmap = {} #val : index

    #     for i , n in enumerate(nums):
    #         diffs = target - n
    #         if diffs in hashmap:
    #             return [hashmap[diffs],i]
    #         hashmap[n] = i
    #     return
    # # time and space-O(n)