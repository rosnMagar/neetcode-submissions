class LRUCache:

    # using the double LL approach
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.storage = {}
        self.lru, self.mru = Node(0,0), Node(0, 0)
        self.lru.next, self.mru.prev = self.mru, self.lru
    
    def insert(self, node):
        prev, nxt = self.mru.prev, self.mru
        prev.next = nxt.prev = node
        node.next, node.prev = nxt, prev
    
    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        # node.prev, node.next = None, None

    def get(self, key: int) -> int:
        if key not in self.storage.keys():
            return -1
        node = self.storage[key]

        # removing it from the current position and adding it as the mru 
        self.remove(node)
        self.insert(node)

        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.storage.keys():
            self.remove(self.storage[key])

        newNode = Node(key, value)
        self.insert(newNode)
        self.storage[key] = newNode

        if len(self.storage) > self.capacity:
            lru = self.lru.next
            self.remove(lru)
            del self.storage[lru.key]


        return None


class Node:
    def __init__(self, key: None, value: None):
        self.value = value
        self.key = key
        self.prev = None
        self.next = None