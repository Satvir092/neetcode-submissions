class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        intervals.sort(key = lambda i: i[0])
        output = [intervals[0]]

        for start, end in intervals[1:]:

            lastEnd = output[-1][1]

            if start <= lastEnd:

                newInterval = [min(output[-1][0], start), max(lastEnd, end)]

                print(newInterval)
                output.pop()
                output.append(newInterval)

            else:

                output.append([start, end])

        return output




        