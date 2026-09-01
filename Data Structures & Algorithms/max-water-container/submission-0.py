class Solution:
    def maxArea(self, A: List[int]) -> int:
        
        l, r = 0, len(A) - 1
        res = 0

        while l < r:
            area = min(A[l], A[r]) * (r-l)
            res = max(res, area)

            if A[l] < A[r]:
                l += 1
            else:
                r -= 1

        return res