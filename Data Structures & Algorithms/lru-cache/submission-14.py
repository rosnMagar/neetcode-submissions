from collections import deque
class ListNode():
    def __init__(self, key = 0, value = 0, next = None, prev=None):
        self.value = value
        self.next = next
        self.prev = prev
        self.key = key

class LRUCache:
    def __init__(self, capacity: int):
        self.store = {}
        self.lru = ListNode(0, 0)
        self.mru = ListNode(0, 0)
        self.lru.next, self.mru.prev = self.mru, self.lru
        self.capacity = capacity

    def insert(self, node):
        prev, nxt = self.mru.prev, self.mru 
        node.prev, node.next = prev, nxt
        prev.next = nxt.prev = node

    def delete(self, node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev

    def get(self, key: int) -> int:
        if key not in self.store.keys():
            return -1
        
        self.delete(self.store[key])
        self.insert(self.store[key])
        
        return self.store[key].value
        
    def put(self, key: int, value: int) -> None:
        node = ListNode(key, value)
        if key in self.store.keys():
            self.delete(self.store[key])
        
        self.store[key] = node
        self.insert(node)

        if len(self.store) > self.capacity:
            lru = self.lru.next
            self.delete(lru)
            del self.store[lru.key]
        