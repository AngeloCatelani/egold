class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        map ={}
        for n in nums:
            map[n] = 1+ map.get(n,0)
        
        maxV = 0
        res = 0

        for n in map:
            if map[n] > maxV:
                res = n
            else:
                res
            maxV = max(maxV,map[n])
        return res