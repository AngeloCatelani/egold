class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        hashmap = {}
        for n in nums:
            hashmap[n] = 1+ hashmap.get(n,0)

        maxV = 0
        res = 0
        for n in hashmap:
            if hashmap[n] > maxV:
                res = n
            else:
                res
            maxV = max(maxV,hashmap[n])
        return res
