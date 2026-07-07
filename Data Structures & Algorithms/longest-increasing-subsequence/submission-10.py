class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        cache = {}

        def dp(i):
            if i in cache:
                return cache[i]

            res = 1
            for j in range(i + 1, len(nums)):
                if nums[i] < nums[j]:
                    res = max(res, dp(j) + 1)

            cache[i] = res 
            return res
        
        return max(dp(i) for i in range(len(nums)))




        