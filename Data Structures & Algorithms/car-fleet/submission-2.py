class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        """
        Problem:
        sort the positions but at the same time sort 

        No clue how this works

        """

        stack = []
        h = [(position[i], speed[i]) for i in range(len(position))]
        h.sort(reverse=True)

        for pos, s in h:
            t = (target - pos) / s
            stack.append(t)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        
        return len(stack)


        