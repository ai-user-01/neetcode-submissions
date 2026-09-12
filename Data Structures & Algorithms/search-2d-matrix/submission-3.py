class Solution:
    def searchMatrix(self, nums: List[List[int]], target: int) -> bool:

        rows, cols = len(nums), len(nums[0])

        l, r = 0, rows*cols-1
        while l <= r:
            mid = l + (r-l) // 2
            row, col = mid // cols, mid % cols
            if nums[row][col] < target:
                l = mid + 1
            elif nums[row][col] > target:
                r = mid -1
            else:
                return True

        return False