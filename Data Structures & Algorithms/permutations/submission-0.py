class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        res = []
        
        def perm(i):
            if len(i) == len(nums):
                p = [nums[k] for k in i]
                res.append(p)
                return
            for j in range(0, len(nums)):
                if j not in i:
                    i.append(j)
                    perm(i)
                    i.pop()

        perm([])
        return res