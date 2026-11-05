class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals.sort()

        res = [intervals[0]]

        for s, e in intervals:

            last = res[-1][1]

            if s <= last:
                res[-1][1] = max(last, e)
            else:
                res.append([s, e])

        return res
