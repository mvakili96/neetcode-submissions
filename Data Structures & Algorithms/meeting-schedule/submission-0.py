"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        starts = []
        ends = []
        for meeting in intervals:
            starts.append(meeting.start)
            ends.append(meeting.end)
        
        intervals = sorted(zip(starts, ends))

        for i in range(1,len(intervals)):
            if intervals[i][0] - intervals[i-1][1] < 0:
                return False

        return True



