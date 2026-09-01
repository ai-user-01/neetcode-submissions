class Solution:
    def search(self, A: List[int], target: int) -> int:
        l, r = 0, len(A)-1

        while l <= r:
            mid = l + ((r-l) // 2)
            if A[mid] == target:
                return mid
            elif A[mid] < target:
                l = mid + 1
            elif A[mid] > target:
                r = mid - 1

        return -1