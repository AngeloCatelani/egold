class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        # can do binary search
        l = 1;
        r = num;
        while l <= r:
            m = (l+r)//2;
            square = m*m;
            if square == num:
                return True;
            elif square < num:
                l = m+1;
            else:
                r = m-1;
        return False;
        