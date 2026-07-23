class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        smap = [[-1] * len(text1) for i in range(len(text2))]

        def rec(r, c):
            if r >= len(text2) or c >= len(text1):
                return 0
            if smap[r][c] != -1:
                return smap[r][c]
            res = 0
            if text1[c] == text2[r]:
                res += rec(r + 1, c + 1) + 1
            else:
                res += max(rec(r + 1, c), rec(r, c + 1))
            smap[r][c] = res
            return res
        
        return rec(0, 0)