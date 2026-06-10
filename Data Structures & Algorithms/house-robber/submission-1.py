class Solution:
    def rob(self, nums: List[int]) -> int:
        cache = [-1] * len(nums)

        def dfs(i):
            if i >= 0 and cache[i] != -1:
                return cache[i]
            if i < 0:
                return 0
            if i < 2:
                cache[i] = nums[i]
                return cache[i]
           
            m = max(dfs(i - 2), dfs(i - 3)) + nums[i]
            cache[i] = m

            return m
        
        return max(dfs(len(nums) - 1), dfs(len(nums) - 2))
            

