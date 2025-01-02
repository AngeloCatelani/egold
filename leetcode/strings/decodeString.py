# def decodeString( s: str) -> str:
#         stack=[]
#         for i in range(len(s)):
#             if s[i] !="]":
#                 stack.append(s[i])
#             else:
#                 substr=""
#                 while stack[-1] !="[":
#                     substr = stack.pop() + substr
#                 stack.pop()

#                 k=""
#                 while stack and stack[-1].isdigit():
#                     k = stack.pop() + k
#                     stack.append(int(k) * substr)
#         return "".join(stack)
# print(decodeString("100[leetcode]"))

def decodeString( s: str) -> str:
        stack = []  # (prevStr, repeatCount)
        currStr = ''
        currNum = 0

        for c in s:
          if c.isdigit():
            currNum = currNum * 10 + int(c)
          else:
            if c == '[':
              stack.append((currStr, currNum))
              currStr = ''
              currNum = 0
            elif c == ']':
              prevStr, num = stack.pop()
              currStr = prevStr + num * currStr
            else:
              currStr += c

        return currStr
print(decodeString("100[leetcode]"))