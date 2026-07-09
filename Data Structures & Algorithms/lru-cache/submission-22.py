class ListNode:
    def __init__(self, val = 0, key = 0, prev = None, nxt = None):
        self.val, self.key, self.prev, self.nxt = val, key, prev, nxt
class LRUCache:

    # (LRU)--> 2 -- 4 <--> 5 -- 3 -- 6 --(MRU)

    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity
        self.lru, self.mru = ListNode(0, 0), ListNode(0, 0)
        self.lru.nxt, self.mru.prev = self.mru, self.lru

    def insert(self, node):
        prev, nxt = self.mru.prev, self.mru
        node.prev, node.nxt = prev, nxt
        prev.nxt = nxt.prev = node

    def delete(self, node):
        prev, nxt = node.prev, node.nxt
        prev.nxt, nxt.prev = nxt, prev

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        self.delete(self.cache[key])
        self.insert(self.cache[key])

        return self.cache[key].val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.delete(self.cache[key])

        node = ListNode(value, key)
        self.insert(node)
        self.cache[key] = node

        if len(self.cache) > self.capacity:
            k = self.lru.nxt.key
            self.delete(self.lru.nxt)
            del self.cache[k]


        
