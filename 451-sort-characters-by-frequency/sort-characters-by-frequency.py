class Solution:
    def frequencySort(self, s: str) -> str:
        count = Counter(s)
        buckets = defaultdict(list) #mapping frequency to char

        for char,value in count.items():
            buckets[value].append(char)
        
        res = []
        for i in range(len(s), 0 , -1):
            for c in buckets[i]:
                res.append(c*i)
        return "".join(res)
        