"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
from heapq import *
class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        meetings = [(i.start, i.end) for i in intervals]
        meetings.sort()

        last_end = -1
        for m in meetings:
            start, end = m
            if start < last_end:
                return False
            last_end = end
        return True