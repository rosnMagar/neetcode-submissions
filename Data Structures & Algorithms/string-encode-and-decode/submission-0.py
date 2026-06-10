class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for word in strs:
            res += str(len(word)) + "#" + word
        return res

    def decode(self, s: str) -> List[str]:
        pointer = 0
        res = []
        while pointer < len(s):
            j = pointer
            while s[j] != "#":
                j += 1
            length = int(s[pointer:j])
            res.append(s[j + 1: j + length + 1])
            j += length + 1
            pointer = j 
        
        return res

        # neet code love you
        # 4#neet4#code4#love3#you
        # 
