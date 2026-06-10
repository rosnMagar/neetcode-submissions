class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def backtrack(n, j, i = 0):

            if i >= len(n):
                res.append(j)
                return

            r = j.copy()
            j.append(n[i]) 
            l = j.copy()

            backtrack(n, l, i + 1)
            backtrack(n, r, i + 1)
            return


        backtrack(nums, [], 0)
        return res
    