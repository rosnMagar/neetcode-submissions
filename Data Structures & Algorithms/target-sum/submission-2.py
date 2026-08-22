class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # 2d dp coding

        dp = [[0 for j in range(-sum(nums), sum(nums) + 1)] for i in range(0, len(nums) + 1)]
        n = len(nums)
        start = sum(nums)

        if abs(target) > start:
            return 0

        dp[0][start] = 1

        for i in range(n):
            for j in range(0, len(dp[i])):
                item = dp[i][j]
                if item != 0:
                    dp[i + 1][j - nums[i]] += dp[i][j]
                    dp[i + 1][j + nums[i]] += dp[i][j]
        
        return dp[n][start + target]


            