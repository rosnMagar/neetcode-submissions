class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        def dfs(curr, i):
            if i == len(nums):
                res.append(curr.copy())
                return
            curr.append(nums[i])
            dfs(curr, i + 1)
            curr.pop()
            
            while i < (len(nums) - 1) and nums[i] == nums[i + 1]:
                i += 1

            # curr.append(nums[i])
            dfs(curr, i + 1)

        dfs([], 0)

        return res


            


