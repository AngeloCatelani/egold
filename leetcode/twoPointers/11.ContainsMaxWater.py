def maxArea(self, height: List[int]) -> int:
        # using two pointers
        # l = 0 r =len(height)-1
        #  3 conditions
        #   l==r (move either one of the pointer)
        #  l<r increment l+=1
        #  r>l decrement r-=1
        #  rectangle area = l*b
        #  area = (r-l) * min(height[l], height[r])
        #  res = max(res,area)

        res = 0
        l = 0
        r = len(height)-1
        while l<r:
            area = (r-l) * min(height[l],height[r])
            res = max(area,res)
            if height[l] < height[r]:
                l+=1
            elif height[r] > height[l]:
                r-=1    
            else:
                r-=1 # or l+=1
        return res

        # time = O(n)