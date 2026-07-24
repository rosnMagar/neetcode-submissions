class Solution:
    def rob(self, nums: List[int]) -> int:
        cache = {}
        l = len(nums)

        if l == 1:
            return nums[0]

        def rec(start, i):
            if i == 1:
                return nums[i]
            if i == 0:
                return 0 if start == (l - 1) else nums[i]
            if i < 0:
                return 0
            if i in cache:
                return cache[i]
            
            cache[i] = max(rec(start, i - 2), rec(start, i - 3)) + nums[i]
            return cache[i]
        
        way1 =  max(rec(l - 1, l - 1), rec(l - 2, l - 2))
        nums = nums[::-1]
        cache = {}
        way2 =  max(rec(l - 1, l - 1), rec(l - 2, l - 2))

        return max(way1, way2)