class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        res =""
        stack = []
        for i in s:
            if stack and stack[-1][0]==i:
                stack[-1][1]+=1

            else:
                stack.append([i,1])
            if stack[-1][1] == k:
                stack.pop()
        for i ,c in stack:
            res += i*c
        return res