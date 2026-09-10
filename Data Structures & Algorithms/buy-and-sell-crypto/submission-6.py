class Solution:
    def maxProfit(self, nums: List[int]) -> int:
        
        res = 0

        l = 0
        for r in range(1, len(nums)):
            while l < r and nums[r] - nums[l] < 0:
                l += 1
            
            res = max(res, nums[r]-nums[l])

        return res