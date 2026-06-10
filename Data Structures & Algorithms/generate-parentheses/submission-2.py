class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        pStack = []

        def dfs(curr, k):
            if len(pStack) == 0 and k == n:
                res.append(curr)
                return

            if k < n:
                pStack.append("(")
                dfs(curr + "(", k + 1)
                pStack.pop()
            
            if len(pStack):
                if pStack[-1] == "(":
                    pStack.pop()
                    dfs(curr + ")", k)
                    pStack.append("(")

        dfs("", 0)

        return res

            
