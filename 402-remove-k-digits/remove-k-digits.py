class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        n = len(num)-k
        res =""

        for i in num:
            while k and stack and stack[-1] > i:
                stack.pop()
                k -=1
            stack.append(i)
        finalNum = "".join(stack[:n])
        return finalNum.lstrip("0") or "0"



