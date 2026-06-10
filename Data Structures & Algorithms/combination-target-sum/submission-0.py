class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        res = []

        def backtrack(v, i = 0, total = 0):
            if i >= len(nums) or total > target:
                return
            if total == target:
                res.append(v.copy())
                return

            v.append(nums[i])
            backtrack(v, i, nums[i] + total)
            v.pop()
            backtrack(v, i + 1, total)
        
        backtrack([])
        return res