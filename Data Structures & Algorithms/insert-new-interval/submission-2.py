class Solution:
    def overlap(self, a, b, c, d):
        return a <= d and c <= b
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        i = 0
        while i < len(intervals):
            a, b = intervals[i]
            c, d = newInterval

            if self.overlap(a, b, c, d):
                newInterval = [min(a, c), max(b, d)]
            else:
                if c < a:
                    res.append(newInterval)
                    res.extend(intervals[i:])
                    return res
                else:
                    res.append(intervals[i])
            i += 1
        
        res.append(newInterval)
        
        return res
