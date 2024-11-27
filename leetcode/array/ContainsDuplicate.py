def containsDuplicate(self, nums: List[int]) -> bool:
        hashmap={}
        for i in range(len(nums)):
            if nums[i] in hashmap.keys():
                return True
            else:
                hashmap[nums[i]] = 1
        return False
