class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        cache = [[-1] * (len(nums) - 1) for i in range(0,2)]

        def dfs(n, i, c):
            if i >= 0 and cache[c][i] != -1:
                return cache[c][i]
            
            # if we start at the final index skip the first one
            if i < 0:
                return 0
            
            if i < 2:
                cache[c][i] = n[i]
                return n[i]

            m = max(dfs(n, i - 2, c), dfs(n, i - 3, c)) + n[i]
            cache[c][i] = m
            return m

        first_include = max(dfs(nums[1:], len(nums) - 2, 0), dfs(nums[1:], len(nums) - 3, 0))
        last_include = max(dfs(nums[:-1], len(nums) - 2, 1), dfs(nums[:-1], len(nums) - 3, 1))
        res = max(first_include, last_include)

        return res

            


