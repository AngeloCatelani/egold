class Solution(object):
    
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        seen = set()  # Track numbers we’ve already seen
        while n != 1 and n not in seen:
            seen.add(n)
            n = self.get_next(n)
        return n == 1
    
    def get_next(self, n):
        sum = 0
        while n > 0:
            digit = n % 10
            sum += digit * digit
            n //= 10  # Reduce n by removing the last digit
        return sum
