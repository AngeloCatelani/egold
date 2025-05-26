def asteroidCollision( asteroids):

        # using stack
        # 3 conditions
        # ==,<,>

        stack = []
        for a in asteroids:
            while stack and stack[-1] > 0 and a<0:
                diff = a + stack[-1]
                if diff<0: # a is greater than stack[-1] element
                  stack.pop()
                elif diff >0: #stack[-1] element is greater than a
                    a =0
                else: #stack[-1] element is equal to a
                    a =0
                    stack.pop()
            if a:
                stack.append(a)
        return stack
print(asteroidCollision([5,10,-5]))
print(asteroidCollision([5,10,-4,-11,9]))