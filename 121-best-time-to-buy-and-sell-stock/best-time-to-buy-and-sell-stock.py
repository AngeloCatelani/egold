class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxL = 0
        l = 0
       
        for r in range(1,len(prices)):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxL = max(profit,maxL)
            else:
                l = r
        return maxL
