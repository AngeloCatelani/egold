class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for i in operations:
            if i == '+' and len(stack) >=2:
                summed = stack[-1]+stack[-2]
                stack.append(summed)
            elif  i == 'D'and len(stack) >=1:
                doubled = stack[-1]*2
                stack.append(doubled)
            elif i == 'C' and len(stack) >=1:
                stack.pop()
            else:
                stack.append(int(i))
        return sum(stack)
        