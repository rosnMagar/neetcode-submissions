class ListNode():
    def __init__(self, key=0, value = 0, prev = None, nxt = None):
        self.key, self.value, self.prev, self.nxt = key, value, prev, nxt

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity
        self.lru = ListNode()
        self.mru = ListNode()
        self.lru.nxt, self.mru.prev = self.mru, self.lru

    def insert(self, node):
        prev, nxt = self.mru.prev, self.mru 
        node.prev, node.nxt = prev, nxt
        prev.nxt = nxt.prev = node
    
    def delete(self, node):
        prev, nxt = node.prev, node.nxt
        prev.nxt, nxt.prev = nxt, prev

    def get(self, key: int) -> int:
        if key in self.cache:
            self.delete(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].value
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.delete(self.cache[key])
        
        node = ListNode(key, value)
        self.insert(node)
        self.cache[key] = node
        
        if len(self.cache) > self.capacity:
            del self.cache[self.lru.nxt.key]
            self.lru = self.lru.nxt