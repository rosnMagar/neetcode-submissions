"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if not intervals:
            return True
        meetings = [(i.start, i.end) for i in intervals]
        heapq.heapify(meetings)

        last_end = -1
        while meetings:
            start, end = heapq.heappop(meetings)
            if start < last_end:
                return False
            last_end = end
        return True