class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        res = len(temperatures) * [0]
        stack = []
        
        for i in range(0, len(temperatures)):
            while stack and temperatures[i] > stack[-1][0]:
                res[stack[-1][1]] = i - stack[-1][1]
                stack.pop()
            stack.append([temperatures[i], i])

        return res