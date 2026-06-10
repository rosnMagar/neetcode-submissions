class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        st = [False] * len(strs)
        m = []
        res = []

        for s in strs:
            tmp = [0] * 26

            for i in s:
                tmp[ord(i) - ord('a')] += 1
            m.append(tmp)
        
        for i in range(0, len(m)):
            tmp = []
            tmp.append(strs[i])

            if not st[i]:
                st[i] = True
                for j in range(i + 1, len(m)):
                    if not st[j] and m[i] == m[j]:
                        st[j] = True
                        tmp.append(strs[j])
                res.append(tmp)
        
        return res
