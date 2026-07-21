class Solution:
    def numDecodings(self, s: str) -> int:
        cache = {}
    
        def dfs(i):
            if i in cache:
                return cache[i]
            if i == len(s):
                cache[i] = 1
                return 1
            x = s[i]
            y = s[i: i + 2]
    
            sm = 0
            if x != "0":
                sm += dfs(i + 1)
            
            if int(y) > 9 and int(y) <= 26:
                sm += dfs(i + 2)
    
            cache[i] = sm 
            return sm
        
        return dfs(0)