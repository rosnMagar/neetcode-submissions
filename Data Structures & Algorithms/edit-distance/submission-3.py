class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp = [[0 for i in range(len(word1) + 1)] for j in range(len(word2) + 1)]

        dp[len(word2)] = [len(word1) - i for i in range(len(word1) + 1)]
        for k in range(len(word2)):   # excludes len(word2), no overwrite
            dp[k][len(word1)] = len(word2) - k


        for i in range(len(word1) - 1, -1, -1):
            for j in range(len(word2) - 1, -1, -1):
                if word1[i] == word2[j]:
                    dp[j][i] = dp[j + 1][i + 1]
                else:
                    dp[j][i] = min(dp[j][i + 1], dp[j + 1][i + 1], dp[j + 1][i]) + 1
        
        return dp[0][0]
        
