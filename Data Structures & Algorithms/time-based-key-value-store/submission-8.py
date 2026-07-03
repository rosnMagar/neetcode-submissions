class TimeMap:

    def __init__(self):
       self.cache = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.cache:
            self.cache[key] = []
        self.cache[key].append((timestamp, value))
        # we store the values in the cache with the timestamp as a tuple  first item is the timestamp

    def get(self, key: str, timestamp: int) -> str:
        # if key exists then 
        # we will have an array of values
        if key not in self.cache:
            return ""
        
        lst = self.cache[key]
        l = 0
        r = len(lst) - 1
        res = ""

        while l <= r:
            m = (l + r) // 2
            if lst[m][0] <= timestamp:
                res = lst[m][1]
                l = m + 1
            else:
                r = m - 1
        return res