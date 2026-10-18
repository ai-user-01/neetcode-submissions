"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda i: i.start)
        last_end = float('-inf')
        for interval in intervals:
            if last_end <= interval.start:
                last_end = interval.end
            else:
                return False
        return True