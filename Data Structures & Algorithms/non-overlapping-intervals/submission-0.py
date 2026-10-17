class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:

        intervals.sort()
        res = 0
        last = intervals[0][1]

        for s, e in intervals[1:]:
            if s < last:
                res += 1
                last = min(e, last)		  		# smaller end value, less chance of overlap
            else:
                last = e

        return res