class Solution:
    def longestPalindrome(self, s: str) -> str:
        # generating all possible subsets of a string is not possible to do in 
        # o(n) time. It is only possible via backtracking in O(2^n) time

        # two pointer with 2nd palindromic chec (inside out method) will find 
        # the solution for this problem in quadratic time

        # have to take care of odd and even numbered inputs

        res = ""

        for i in range(0, len(s)):
            l = i
            r = i

            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r - l + 1 > len(res):
                    res = s[l: r + 1]
                l -= 1
                r += 1

            # for even palindromes
            l = i
            r = i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r - l + 1 > len(res):
                    res = s[l: r + 1]
                l -= 1
                r += 1
   
        return res
            

