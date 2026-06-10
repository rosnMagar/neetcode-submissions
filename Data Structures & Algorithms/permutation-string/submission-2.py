class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s1) > len(s2):
            return False

        memo = [0 for i in range(0, 26)]
        ws = len(s1)
        i = 0

        for l in s1:
            memo[ord(l) - ord('a')] += 1

        while i + (ws - 1) < len(s2):
            match = True
            m = list(memo)
            s = s2[i: i + ws]
            for j in s:
                if m[ord(j) - ord('a')] == 0:
                    match = False
                    break
                m[ord(j) - ord('a')] -= 1
            if match:
                return True
            i += 1
        
        return False