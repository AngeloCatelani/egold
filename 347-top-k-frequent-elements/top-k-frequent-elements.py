class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        hashmap = {}
        freq = [[] for i in range(len(nums)+1)]

        for i in nums:
            hashmap[i] = 1+ hashmap.get(i,0)

        for key,values in hashmap.items():
            freq[values].append(key)

        for i in range(len(freq)-1,0,-1):
            # print(freq) [[], [3], [2], [1], [], [], []]
            for n in freq[i]:
                # print(n)
                res.append(n)
                if len(res) == k:
                    return res