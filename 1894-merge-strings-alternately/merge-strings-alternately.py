class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        if not word1:
            return word2
        if not word2:
            return word1
        l = 0
        r = 0
        s = ""
        while l < len(word1) and r < len(word2):
            s +=(word1[l])
            s+=(word2[r])
            l+=1
            r+=1
             # Append remaining characters from word1
        while l < len(word1):
            s += word1[l]
            l += 1
        
        # Append remaining characters from word2
        while r < len(word2):
            s += word2[r]
            r += 1
        
        return s