class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for i in range(32):
            b = n & 1
            n = n >> 1 
            res = res << 1
            res = res | b
        return res