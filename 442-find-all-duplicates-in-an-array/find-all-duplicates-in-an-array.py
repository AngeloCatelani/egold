class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        hashmap = {}
        arr =[]
        for n in nums:
            hashmap[n] = 1+ hashmap.get(n,0)
        for n , count in hashmap.items():
            if count >= 2:
                arr.append(n)
        return arr
        