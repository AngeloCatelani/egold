class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0;
        maxL = 0;
        for r in range(1,len(prices)):
            if prices[l]  < prices[r]:
                profit = prices[r]- prices[l];
                maxL = max(maxL,profit); 
            else:
                l=r;
        return maxL;
        