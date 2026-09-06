class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 0
        res = 0

        for r in range(len(prices)):
            while prices[r] < prices[l]:
                l += 1
            
            profit = prices[r] - prices[l]
            
            res = max(res, profit)

        return res