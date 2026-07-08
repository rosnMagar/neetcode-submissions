class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(n, s):
            if len(n) == len(nums):
                return res.append(n[:])
            
            for num in nums:
                if num not in s:
                    n.append(num)
                    s.add(num)
                    backtrack(n, s)
                    n.pop()
                    s.remove(num)

        backtrack([], set([])) 
        return res

