class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for i in operations:
            if i == "+"and len(stack) >=2:
                t1 = stack[-1]
                t2 = stack[-2]
                stack.append((t1+t2))
            elif i == "D"and len(stack) >=1:
                t1 = stack[-1]
                stack.append((t1*2))
            elif i == "C"and len(stack) >=1:
                stack.pop()
            else:
                stack.append(int(i))
        return sum(stack)