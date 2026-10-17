class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        intervals.sort(key = lambda i : i[0])				#O(nlogn)
        res = [intervals[0]]							#[[1, 3]]

        for s, e in intervals[1:]:
            lastEnd = res[-1][1]						#[[1, 3]]

            if s <= lastEnd:							#2 <= 3
                res[-1][1] = max(lastEnd, e)				#[[1, 6]]
            else:
                res.append([s, e])						#8 > 6
                                            #[[1, 6], [8,10]]
        return res
