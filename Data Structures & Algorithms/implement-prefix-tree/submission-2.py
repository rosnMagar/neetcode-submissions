class Node:
    def __init__(self, val = None, nxt = None, end = False):
        self.val = val
        self.nxt = nxt
        self.end = end
        
class PrefixTree:

    def __init__(self):
        self.store = Node(-1, {})

    def insert(self, word: str) -> None:
        curr = self.store
        for i, w in enumerate(word):
            final = i == len(word) - 1
            if w in curr.nxt:
                curr = curr.nxt[w]
                if i == len(word) - 1:
                    curr.end = final
            else:
                curr.nxt[w] = Node(w, {}, final)
                curr = curr.nxt[w]

    def search(self, word: str) -> bool:
        curr = self.store
        for w in word:
            if w in curr.nxt:
                curr = curr.nxt[w]
            else:
                return False
        return curr.end

    def startsWith(self, prefix: str) -> bool:
        curr = self.store
        for w in prefix:
            if w in curr.nxt:
                curr = curr.nxt[w]
            else:
                return False
        return True
        
        