class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lo = 0
        hi = len(nums) - 1

        while lo <= hi:
            p = (hi + lo) // 2
            if nums[p] == target:
                return p
            if nums[p] < target:
                lo = p + 1
            else:
                hi = p - 1
        return -1

