class Solution:
    def partitionString(self, s: str) -> int:
        res = 1
        hashset = set()
        for i in s:
            if i in hashset:
                res +=1
                hashset = set()
                hashset.add(i)
            else:
                hashset.add(i)
        return res

        # time O(n)
        # space O(1)