class Solution:
    def insert(self, A: List[List[int]], B: List[int]) -> List[List[int]]:
        res = []

        for i in range(len(A)):
            if B[1] < A[i][0]:
                res.append(B)
                return res + A[i:]
            elif B[0] > A[i][1]:
                res.append(A[i])
            else:
                B = [min(B[0], A[i][0]), max(B[1], A[i][1])]

        res.append(B)
        return res
