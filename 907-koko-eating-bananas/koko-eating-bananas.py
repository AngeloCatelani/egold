class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1  # Initialize the left boundary of binary search (smallest possible eating speed)
        r = max(piles)  # Initialize the right boundary of binary search (largest possible eating speed)
        res = r  # Initialize the result with the maximum eating speed
        
        # Binary search loop
        while l <= r:  
            m = (l + r) // 2  # Calculate the mid-point of current search boundaries (potential eating speed)
            totalTime = 0  # Initialize total time to eat all piles at speed m
            
            # Calculate the total hours needed to eat all bananas at speed m
            for p in piles:
                totalTime += math.ceil(float(p) / m)  # Use math.ceil to round up to the nearest integer
                
            # If totalTime is within allowed hours h
            if totalTime <= h:
                res = m  # Update result to current mid-point (as it's a potential answer)
                r = m - 1  # Try for a smaller eating speed in the next iteration
            else:
                l = m + 1  # If totalTime exceeds h, try for a larger eating speed in the next iteration
                
        return res  # Return the minimum eating speed found
