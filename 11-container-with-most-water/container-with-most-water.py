class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l = 0
        r =len(height)-1
        maxL = 0
        while  l < r:
            area = r-l
            maxL = max(maxL,area * min(height[r],height[l]))
            if height[l] <= height[r]:
                
                l +=1
            else:
                r-=1
        return maxL
