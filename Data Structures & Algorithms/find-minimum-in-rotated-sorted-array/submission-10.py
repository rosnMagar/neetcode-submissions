class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r =  len(nums) - 1

        if len(nums) == 1:
            return nums[0]

        while l < r:
            if r - l == 1:
                return min(nums[r], nums[l])
            m = (l + r) // 2
            if nums[r] < nums[m]:
                l = m
            elif nums[l] > nums[m]:
                r = m
            # already ordered
            else:
                return nums[0]