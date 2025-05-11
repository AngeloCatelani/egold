def asteroidCollision( asteroids):
        stack = []
        for n in asteroids:
            if n > 0:
                stack.append(n)
            if n < 0:
                if stack[-1] < n or stack[-1] ==n :
                    stack.pop()
                else:
                     stack.append(n)
            
        return stack
print(asteroidCollision([5,10,-5]))