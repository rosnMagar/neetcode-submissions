class Solution:
    def rob(self, nums: List[int]) -> int:
        cache = {}

        def rec(i):
            if i < 0:
                return 0
            if i <= 1:
                return nums[i]
            if i in cache:
                return cache[i]
            
            cache[i] = max(rec(i - 2), rec(i - 3)) + nums[i]
            return cache[i]
        
        return max(rec(len(nums) - 1), rec(len(nums) - 2))
