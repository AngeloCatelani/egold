class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        countS = {};
        l = 0;
        res = 0;
        for r in range (len(s)):
            countS[s[r]] = 1+ countS.get(s[r],0);
            while countS[s[r]] > 2:
                countS[s[l]] -=1;
                l+=1;
            res = max(res,r-l+1);
        return res;

