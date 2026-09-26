class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda i:i[0])

        last_end = intervals[0][1]
        output = 0

        for start, end in intervals[1:]:

            if start < last_end:

                if end > last_end:

                    pass

                else:

                    last_end = end

                output += 1

            else:

                last_end = end

        return output



