class Solution:
    def removeStars(self, s: str) -> str:
        stack = []
        stri = ""
        for i in range(len(s)):
            while stack and stack[-1] == '*':
                stack.pop()
                stack.pop()
            stack.append(s[i])
            if stack[-1] == "*":
                stack.pop()
                stack.pop()

        for i in stack:
            stri+=i
        return stri

        