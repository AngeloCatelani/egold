class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        if len(position) <= 1:
            return len(position)

        # Combine position and speed and sort based on the position
        cars = sorted(zip(position, speed), key=lambda x: x[0], reverse=True)
        # print(cars)  [(10, 2), (8, 4), (5, 1), (3, 3), (0, 1)]

        stack = []
        for pos, spd in cars:
            time = (target - pos) / spd
            if not stack or time > stack[-1]:
                stack.append(time)

        return len(stack)
