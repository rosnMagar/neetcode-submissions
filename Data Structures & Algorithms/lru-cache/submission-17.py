class ListNode:
    def __init__(self, key, value, prev = None, nxt = None):
        self.value = value
        self.prev = prev
        self.next = nxt
        self.key = key

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.mru = ListNode(0, 0) 
        self.lru = ListNode(0, 0)
        self.mru.prev = self.lru
        self.lru.next = self.mru
        self.cache = {}
    
    def insert(self, node):
        prev, nxt = self.mru.prev, self.mru
        nxt.prev, node.next = node, nxt
        prev.next, node.prev = node, prev


    def delete(self, node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        self.delete(self.cache[key]) 
        self.insert(self.cache[key])

        return self.cache[key].value

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.delete(self.cache[key])
        
        node = ListNode(key, value)
        self.insert(node)
        self.cache[key] = node

        if len(self.cache) > self.capacity:
            del self.cache[self.lru.next.key]
            self.lru = self.lru.next
        
