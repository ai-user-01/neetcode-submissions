class Solution:
    def searchMatrix(self, nums: List[List[int]], target: int) -> bool:
        
        rows, cols = len(nums), len(nums[0])

        l, r = 0, (rows*cols)-1
        while l <= r:
            m = l + (r-l)

            r, c = m // cols, m % cols

            if nums[r][c] < target:
                l = m + 1
            elif nums[r][c] > target:
                r = m - 1
            else:
                return True

        return False