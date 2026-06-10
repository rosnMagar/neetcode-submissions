class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        output = []

        def par(p, l, r, n):
            if l < n:
                par(p + "(", l + 1, r, n)
            if r < l:
                par(p + ")", l, r + 1, n)
            
            if r == l and r == n: 
                output.append(p)
        
        par("(", 1, 0, n)
        
        return output