class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        maxL = 0
        for i in range(1,len(prices)):
            if prices[i]> prices[i-1]:
                maxL += max(0,prices[i]-prices[i-1])
        return maxL