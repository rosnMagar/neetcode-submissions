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
        for w in word:
            if w not in curr.nxt:
                curr.nxt[w] = Node(w, {})
            curr = curr.nxt[w] 
        curr.end = True

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
        
        