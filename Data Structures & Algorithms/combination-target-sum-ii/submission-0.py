class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort() 
        res = []

        def dfs(curr, s, i):
            if s == target:
                res.append(curr.copy())
                return

            if s > target or i == len(candidates):
                return 

            curr.append(candidates[i])
            dfs(curr, s + candidates[i], i + 1)
            curr.pop()

            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1
            dfs(curr, s, i + 1)

        dfs([], 0, 0)
        return res
