class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        m = -9e9
        s = 0

        for n in nums:
            if s < 0:
                s = n
                continue
            s += n
            m = max(s, m)
        
        return max(s, m)