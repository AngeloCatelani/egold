class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        
        for i in asteroids:
            while stack and i < 0 < stack[-1]:
                if stack[-1] < -i:
                    stack.pop()
                    continue  # Continue checking the next element in the stack
                elif stack[-1] == -i:
                    stack.pop()
                    break  # Both are destroyed, exit the loop
                break  # Current asteroid is destroyed, exit the loop
            else:
                stack.append(i)  # Append the asteroid if no collision occurs
                
        return stack
