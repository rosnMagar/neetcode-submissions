class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if not len(nums):
            return 0

        v = [False] * len(nums)
        s = defaultdict(int)
        res = 1

        for i in range(len(nums)):
            s[nums[i]] = i
        
        for i in range(len(nums)):
            r = 1
            nxt = nums[i] + 1
            while nxt in s.keys():
                r += 1 
                res = max(res, r)
                nxt += 1
        
        return res