class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        l = 0
        r = int(c ** 0.5)
        while l <= r:
            if l*l + r*r == c:
                return True
            if l*l + r*r > c:
                r -=1
            else:
                l += 1
        return False

            