def maxDepth(s: str) -> int:
        stack = []
        maxDepth = 0
        for c in s:
            # print(c)
            if c == "(":
                stack.append(c)
                maxDepth = max(maxDepth,len(stack))

            elif c == ")":
                stack.pop()
        return maxDepth
    # Time Complexity: O(N).
# Space Complexity: O(N).
print(maxDepth("(1+(2*3)+((8)/4))+1"))