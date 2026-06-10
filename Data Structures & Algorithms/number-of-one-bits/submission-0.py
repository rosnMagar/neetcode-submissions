class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0

        for i in range(0, 32):
            if (2 ** i) & n:
                res += 1

        return res