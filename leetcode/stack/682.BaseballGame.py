def calPoints( operations) -> int:
        # i==integer continue
        # + add previous two
        # D -> 2*i
        # C -> pop()
        # output-> sum
        stack = []
        sum = 0
        for i in operations:
            # print(i)
            
            if i == "C":
                stack.pop()
            elif i =="D":
                stack.append((int(stack[-1])*2))
            elif i =="+":
                stack.append(((stack[-1])+ stack[-2]))
            elif i != "C" or i != "D" or i != "+":
                stack.append(int(i))
        for i in range(len(stack)):
            print(stack)
            sum+=stack[i]
        return sum
print(calPoints(["5","2","C","D","+"]))