class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        s =list(s)
        n = len(s)

        for i in range(0,n,2*k):
            l = i
            r = min(n-1,i+k-1)
            while l<r:
                s[l],s[r] = s[r],s[l]
                l+=1
                r-=1
        return "".join(s)
        