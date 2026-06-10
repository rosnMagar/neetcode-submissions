class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        c = {}

        def dfs(i):
            if i in c.keys():
                return c[i]

            if len(s[i:]) == 0:
                c[i] = True
                return True

            t = False
            for word in wordDict:
                if s[i: i + len(word)] == word:
                    res = dfs(i + len(word))
                    c[i] = res
                    t = t or res
            return t

        return dfs(0)
            


