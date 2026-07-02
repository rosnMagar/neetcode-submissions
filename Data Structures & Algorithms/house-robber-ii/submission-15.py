class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        dp = {} 
        def rec(n, skip):
            if skip and n == 0:
                return 0
            if n in dp:
                return dp[n]
            if n < 0:
                return 0

            dp[n] = max(rec(n - 2, skip), rec(n - 3, skip)) + nums[n]
            return dp[n]

        m1 = max(rec(len(nums) - 1, True), rec(len(nums) - 2, False))
        nums.reverse()
        dp = {}
        m2 = max(rec(len(nums) - 1, True), rec(len(nums) - 2, False))

        return max(m1, m2)
            