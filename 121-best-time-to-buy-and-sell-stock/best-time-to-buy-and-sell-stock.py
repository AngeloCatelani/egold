class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        maxL = 0
        for r in range(1,len(prices)):
            if prices[l] < prices[r]:
                maxL = max(maxL,prices[r]-prices[l])
            else:
                l = r
        return maxL