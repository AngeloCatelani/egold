class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res =[]
        hashmap = {}
        freq = [[] for i in range(len(nums)+1)]

        for i in nums:
            if i not in hashmap:
                hashmap[i] = 1
            else:
                hashmap[i] +=1
        
        for keys,values in hashmap.items():
            freq[values].append(keys)
        
        for i in range(len(freq)-1,0,-1):
            for n in freq[i]:
                # print(n,"n",freq,"freq") [[], [3], [2], [1], [], [], []] freq , n =1
                res.append(n)
                if len(res) == k:
                    return res
        

        # time = O(n)