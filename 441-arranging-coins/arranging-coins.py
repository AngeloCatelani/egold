class Solution:
    def arrangeCoins(self, n: int) -> int:
        # Initialize the left and right boundaries for binary search
        l, r = 1, n
        
        # Initialize the result variable to store the maximum number of complete rows
        res = 0
        
        # Perform binary search
        while l <= r:
            # Calculate the midpoint of the current search range
            mid = (l + r) // 2
            
            # Calculate the number of coins required to form 'mid' complete rows
            # Using the formula for the sum of the first 'mid' natural numbers: mid * (mid + 1) / 2
            coins = (mid / 2) * (mid + 1)
            
            # If the calculated coins exceed the given number of coins 'n'
            if coins > n:
                # Adjust the right boundary to search in the lower half
                r = mid - 1
            else:
                # If the calculated coins are within the limit
                # Adjust the left boundary to search in the upper half
                l = mid + 1
                # Update the result to the maximum number of complete rows found so far
                res = max(mid, res)
        
        # Return the maximum number of complete rows that can be formed
        return res
