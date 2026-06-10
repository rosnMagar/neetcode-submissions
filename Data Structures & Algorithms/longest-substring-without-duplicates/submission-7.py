class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        # set([a, b, c]) = s
        # res = len(s) = 3
        # a a a a b c d e a
        #         |
        #                 |                 

        lo, hi = 0, 0
        tset = set()
        res = 0
        
        while hi <= len(s) - 1:
            if s[hi] not in tset or lo == hi:
                tset.add(s[hi])
                res = max(res, len(tset))
                hi += 1
            else:
                tset.remove(s[lo])
                lo += 1

        return res
        