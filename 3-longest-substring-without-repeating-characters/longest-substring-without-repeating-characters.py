class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashset = set()
        l=0
        maxL = 0
        for r in range(len(s)):
            while s[r] in hashset:
                hashset.remove(s[l])
                l+=1
            else:
                hashset.add(s[r])
            maxL = max(maxL,r-l+1)
        return maxL
         