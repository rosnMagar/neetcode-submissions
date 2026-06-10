class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = defaultdict(list)
        for s in strs:
            c = [0] * 26
            for char in s:
                c[ord(char) - ord("a")] += 1
            anagram_map[tuple(c)].append(s)
        
        return list(anagram_map.values())

        
        