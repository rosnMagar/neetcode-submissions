from heapq import *

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        heapify(intervals)
        res = []

        while len(intervals) > 1:
            a, b = heappop(intervals)
            c, d = intervals[0] 

            if a <= d and c <= b:
                heappop(intervals)
                heappush(intervals, [min(a, c), max(b, d)])
            else:
                res.append([a, b])
        
        res.append(intervals[0])
            
        return res