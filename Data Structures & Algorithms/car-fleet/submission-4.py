class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # retry on Jun 10th, 2026
        lst = list(zip(position, speed))
        lst.sort()
        stack = []

        for i in reversed(lst):
            d = target - i[0]
            t = d / i[1]

            if not stack or stack[-1] <  t:
                stack.append(t)
            
        return len(stack)


        