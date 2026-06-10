class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0

        maxLength = 0
        strMap = defaultdict()

        # "ifyoucancodethis"
        # "if"

        for r in range(len(s)):
            if s[r] in strMap.keys():
                l = max(strMap[s[r]] + 1, l)
            maxLength = max(maxLength, r - l + 1)
            strMap[s[r]] = r
        return maxLength






        