class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        hashmap = {}
        freq = [[]    for i in range(len(nums)+1)]
        res = []

        for i in nums:
            hashmap[i] = 1+ hashmap.get(i,0)
        
        for key,values in hashmap.items():
            freq[values].append(key)

        for i in range(len(freq)-1,0,-1):
            for char in freq[i]:
                res.append(char)
                if len(res)==k:
                    return res
