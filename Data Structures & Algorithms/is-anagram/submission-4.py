class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        c1 = [0] * 26
        c2 = [0] * 26

        for i in range(0, len(s)):
            c1[ord(s[i]) - ord("a")] += 1
            c2[ord(t[i]) - ord("a")] += 1

        return c1 == c2 

