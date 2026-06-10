class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = -9e9
        curr = 0

        for n in nums:
            curr = curr + n
            res = max(curr, res)
            if curr < 0:
                curr = 0
        
        return res


        