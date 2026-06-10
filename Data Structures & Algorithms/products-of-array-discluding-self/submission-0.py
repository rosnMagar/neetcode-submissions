class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        # first pass

        sl = [1] * len(nums)
        sr = [1] * len(nums)
        res = []

        i = 1 
        j = len(nums) - 2

        while i < len(nums) and j >= 0:
            sl[i] = nums[i - 1] * sl[i - 1]
            sr[j] = nums[j + 1] * sr[j + 1] 

            i = i + 1
            j = j - 1
            
        for i in range(0, len(sl)):
            res.append(sl[i] * sr[i])
        
        return res
        
            

