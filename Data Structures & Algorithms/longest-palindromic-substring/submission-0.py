class Solution:
    ####
    #### PRACTICE!!!!!!! TWO POINTERS is BETTER FOR THIS ONE
    ####
    def longestPalindrome(self, s: str) -> str:
        res = 0
        resIdx = 0
        for i in range(len(s)):
            # for odd
            l = i
            r = i

            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > res:
                    res = r - l + 1
                    resIdx = l
                l -= 1
                r += 1
            
            # even length
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > res:
                    res = r - l + 1
                    resIdx = l
                l -= 1
                r += 1
            
        return s[resIdx: resIdx + res]