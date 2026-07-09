class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # can't re-use the same indices 
        # track using some sort of a set 

        res = []
        candidates.sort()

        def backtrack(i, s):
            if sum(s) == target:
                res.append(s[:])
                return
            if sum(s) > target or i == len(candidates):
                return

            s.append(candidates[i])
            backtrack(i + 1, s)
            s.pop()

            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1
            backtrack(i + 1, s)
        
        backtrack(0,[])
        return res

            
