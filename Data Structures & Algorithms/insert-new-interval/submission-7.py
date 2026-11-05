class Solution:
    def insert(self, A: List[List[int]], B: List[int]) -> List[List[int]]:
        
        res = []
        
        for i in range(len(A)):
            if A[i][0] > B[1]:
                res.append(B)
                return res + A[i:]
            elif A[i][1] < B[0]:
                res.append(A[i])
            else:
                B = [min(A[i][0], B[0]), max(A[i][1], B[1])]

        res.append(B)
        return res
        
