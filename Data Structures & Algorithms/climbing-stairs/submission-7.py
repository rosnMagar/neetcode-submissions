class Solution:
    def climbStairs(self, n: int) -> int:
        cache = {}

        def rec(i):
            if i <= 1:
                return 1
            if i in cache:
                return cache[i]
            cache[i] = rec(i - 1) + rec(i - 2)
            return cache[i]

        return rec(n) 