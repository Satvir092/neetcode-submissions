"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:

        intervals_ar = []
        
        for interval in intervals:

            intervals_ar.append([interval.start, interval.end])

        intervals_ar.sort()

        if not intervals_ar:
            return True

        last_end = intervals_ar[0][1]

        for start, end in intervals_ar[1:]:

            if start < last_end:

                return False

            else:

                last_end = end

        return True
