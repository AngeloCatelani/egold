class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hashmap = {}
        count =0
        l = 0
        maxL = 0
        res = 0
        for r in range(len(s)):
            hashmap[s[r]] = 1+ hashmap.get(s[r],0)
            maxL = max(maxL,hashmap[s[r]])
            while (r-l+1)-maxL > k:
                hashmap[s[l]]-=1
                l+=1
            res = max(res,r-l+1)
        return res


        