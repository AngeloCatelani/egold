class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        l = 0
        maxL = 0
        for i in range(1,len(prices)):
            if prices[l] < prices[i]:
                maxL = max(maxL,prices[i] - prices[l])
            else:
                l = i
        return maxL
