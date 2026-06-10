class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = -9e9
        curr_sum = 0

        for n in nums:
            curr_sum += n
            res = max(res, curr_sum)
            if curr_sum < 0:
                curr_sum = 0
    
        return res


        