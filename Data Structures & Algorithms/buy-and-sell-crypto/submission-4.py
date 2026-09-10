class Solution:
    def maxProfit(self, nums: List[int]) -> int:
        # l, r = 0, 1
        # maxP = 0

        # while r < len(prices):
        #     if prices[l] < prices[r]:
        #         profit = prices[r] - prices[l]
        #         maxP = max(maxP, profit)
        #     else:
        #         l = r
        #     r += 1
        # return maxP
        
        res = 0
        
        l = 0
        for r in range(1, len(nums)):
            while l < r and nums[l] > nums[r]:   	# check with r (while window-not-valid)
                l += 1                                	# remove/move l

            local_res = nums[r] - nums[l]
            res = max(res, local_res)

        return res
