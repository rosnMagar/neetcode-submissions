class Solution:
    def climbStairs(self, n: int) -> int:
        # using dynamic programming

        left = 1
        right = 1
        i = n - 2
        while i >= 0:
            tmp = left
            left = left + right
            right = tmp
            i -= 1

        return left

