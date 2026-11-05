class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        res = 0

        last_end = intervals[0][-1]

        for s, e in intervals[1:]:
            if last_end > s:
                res += 1
                last_end = min(last_end, e)
            else:
                last_end = e

        return res