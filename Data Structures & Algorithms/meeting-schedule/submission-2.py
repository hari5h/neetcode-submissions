"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key = lambda i:i.start) #asc

        for i in range(len(intervals)-1):
            #i vs i+1
            start = intervals[i].start
            end = intervals[i].end

            start1 = intervals[i+1].start
            end1 = intervals[i+1].end

            if end > start1: 
                return False

        return True



