class Solution:
    def jump(self, nums: List[int]) -> int:
        """
        DP method
        """

        dp = defaultdict()
        dp[len(nums) - 1] = (True, 0)

        for i in range(len(nums) - 2, -1, -1):
            dp[i] = (False, 1000)
            for j in range(nums[i] + i, i, -1):
                if j in dp.keys() and dp[j][0]:
                    tr, ind = dp[j]
                    idx = min(dp[i][1], ind + 1)
                    dp[i] = (True, idx)
        
        return dp[0][1]
        