class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        # Helper function to check if the given capacity 'max_capacity' is enough
        # to ship all the packages within 'days' days
        def can_ship_with_capacity(max_capacity):
            current_weight, day_count = 0, 1  # Initialize current total weight and day count
            # Loop through the weights of the packages
            for weight in weights:
                current_weight += weight  # Add package weight to current load
                # If the current load exceeds the max capacity, start a new day
                # and reset the current load to the current package's weight
                if current_weight > max_capacity:
                    day_count += 1
                    current_weight = weight
            # The capacity is enough if we can ship within required days
            return day_count <= days

        # Define the search space between largest single package and total weight
        left, right = max(weights), sum(weights)
      
        # Use binary search to find the minimum capacity needed to ship within 'days' days
        # The search will find the first value where 'can_ship_with_capacity' returns True
        min_capacity_needed = left + bisect_left(range(left, right), True, key=can_ship_with_capacity)
      
        return min_capacity_needed

# Example usage:
# solution = Solution()
# min_capacity = solution.shipWithinDays([1,2,3,4,5,6,7,8,9,10], 5)
# print(min_capacity)  # Output: 15
        