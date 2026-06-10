class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        mx = 1
        mn = 1
        res = nums[0]
        for n in nums:
            if n == 0:
                mx, mn = n, n
            tmp = mx * n
            mx = max(mx * n, mn * n, n)
            mn = min(tmp, mn * n, n)
            
            res = max(res, mx, mn)
        return res        

