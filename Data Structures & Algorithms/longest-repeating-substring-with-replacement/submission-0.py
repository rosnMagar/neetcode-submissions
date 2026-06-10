class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        count = {}
        res = 0

        l, h = 0, 0

        while h < len(s):
            count[s[h]] = 1 + count.get(s[h], 0)

            while (h - l + 1) - max(count.values()) > k:
                count[s[l]] -= 1
                l += 1

            res = max(res, h - l + 1)
            h += 1
        return res
