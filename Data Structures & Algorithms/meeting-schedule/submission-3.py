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
            int1 = intervals[i]
            int2 = intervals[i+1]

            if int1.end > int2.start: 
                return False

        return True



