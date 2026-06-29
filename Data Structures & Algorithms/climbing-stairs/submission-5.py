class Solution:
    def climbStairs(self, n: int) -> int:
        one, two = 1, 1

        for i in range(n - 1):
            tmp = one
            one = one + two
            two = tmp
        
        return one



        # def rec(s):
        #     if s in cache:
        #         return cache[s]
        #     if s == n:
        #         return 1
        #     if s > n:
        #         return 0
        #     sm = rec(s + 1) + rec(s + 2)
        #     cache[s] = sm
        #     return sm
        
        # return rec(0)
            

