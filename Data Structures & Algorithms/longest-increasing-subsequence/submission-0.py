class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
            
        """
        Brute force method:
        
        start at each number and try to find the next character that is larger than the current one we 
        are selecting.
        
        i.e
        
        start at index 0 (9)
        
        pairs generated: 9 + nothing (largest subsequence if started from here: 1)
        
        start at index 1 (1)
        
        pairs generated: (1, 4)2 (1, 2)3 (1, 3)4 (1, 3)5 (1, 7)6
    
        """

        dp = {}

        def dfs(i):
            if i in dp:
                return dp[i]

            r = 1
            for j in range(i + 1, len(nums)):
                if nums[i] < nums[j]:
                    r = max(dfs(j) + 1, r)

            dp[i] = r
            return r
        
        return max(dfs(i) for i in range(len(nums)))
            

            
            
    








