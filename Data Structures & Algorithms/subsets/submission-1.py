class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []

        def backtrack(prev, iter):
            if iter == len(nums):
                result.append(prev[:])
                return

            tmp = prev[:]
            backtrack(tmp, iter + 1) 
            tmp.append(nums[iter])
            backtrack(tmp, iter + 1) 
        
        backtrack([], 0)

        return result
