class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        # [1, 2, 3]

        # []

        # [1, 2, 3], () -- > [1], [2], [3]
        
        
        # [1], (1) --> [1, 2, 3] --> skip 1 

        # [1, 2], (1, 2) --> -[1, 2, 3] --> 
        # [1, 2, 3] our input arr has reached the length of nums

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

