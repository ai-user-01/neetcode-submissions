class Solution:
    def maxProfit(self, nums: List[int]) -> int:
        
        res = 0

        l = 0
        for r in range(len(nums)):
            while l < r and nums[r] - nums[l] < 0:
                l += 1

            profit = nums[r] - nums[l]
            res = max(res, profit)

        return res