class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        
        # Sort intervals based on the start time
        intervals.sort(key=lambda x: x[0])
        
        # Initialize count for the number of intervals to remove
        count = 0
        
        # Initialize the end time of the first interval
        end_time = intervals[0][1]
        
        for i in range(1, len(intervals)):
            # If the current interval starts before the last interval ends, we have an overlap
            if intervals[i][0] < end_time:
                count += 1
                # Update the end time to be the minimum of the current end times to keep the interval
                # that finishes first (greedy approach to minimize overlaps)
                end_time = min(end_time, intervals[i][1])
            else:
                # No overlap, update the end time to the end of the current interval
                end_time = intervals[i][1]
        
        return count

        