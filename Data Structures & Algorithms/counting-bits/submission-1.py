class Solution:
    def countBits(self, n: int) -> List[int]:
        res = [0] * (n + 1)

        for i in range(n + 1):
            r = 0
            k = i
            for j in range(32):
                r += k & 1
                k = k >> 1
            res[i] = r

        return res
