class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        n = len(num)-k
        for i in num:
            while k and stack and stack[-1] > i:
                stack.pop()
                k-=1
            stack.append(i)
        return "".join(stack[:n]).lstrip("0") or "0"