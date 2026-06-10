class Solution:
    def rob(self, nums: List[int]) -> int:
        
        res = 0
        dp = {}

        def dfs(i):
            if i in dp.keys():
                return dp[i]
            
            if i < 0:
                return 0

            if i < 2:
                return nums[i]
                
            m = max(dfs(i - 2), dfs(i - 3)) + nums[i]
            dp[i] = m

            return m
            
        return max(dfs(len(nums) - 1), dfs(len(nums) - 2))
