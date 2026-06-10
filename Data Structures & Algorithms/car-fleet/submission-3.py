class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        result = 0
        cars = sorted(zip(position, speed))

        stack = []

        for p, s in reversed(cars):
            time = (target - p) / s

            if len(stack) <= 0 or time > stack[-1]:
                stack.append(time) 
        
        return len(stack)
