class Solution {

    public int[][] insert(int[][] intervals, int[] newInterval) {

        // Declare a new list to store the result of the insertion.
        List<int[]> res = new ArrayList<>();

        // Iterate over the input list of intervals.
        for (int[] interval : intervals) {

            // **Line-by-line explanation:**
            // * This for loop iterates over the input list of intervals.

            // Check if the new interval is null or if the end of the current interval is less than the start of the new interval.
            if (newInterval == null || interval[1] < newInterval[0]) {

                // **Line-by-line explanation:**
                // * This if statement checks if the new interval is null or if the end of the current interval is less than the start of the new interval. If either of these conditions is true, then the current interval is added to the result list.

                // Add the current interval to the result list.
                res.add(interval);
            }

            // Otherwise, check if the start of the current interval is greater than the end of the new interval.
            else if (interval[0] > newInterval[1]) {

                // **Line-by-line explanation:**
                // * This else-if statement checks if the start of the current interval is greater than the end of the new interval. If this condition is true, then the new interval is added to the result list, followed by the current interval.

                // Add the new interval to the result list.
                res.add(newInterval);

                // Add the current interval to the result list.
                res.add(interval);

                // Set the new interval to null to indicate that it has been inserted.
                newInterval = null;
            }

            // Otherwise, the new interval overlaps with the current interval.
            else {

                // **Line-by-line explanation:**
                // * This else statement executes if the new interval overlaps with the current interval.

                // Update the start and end points of the new interval to be the minimum and maximum of the start and end points of the new interval and the current interval, respectively.
                newInterval[0] = Math.min(interval[0], newInterval[0]);
                newInterval[1] = Math.max(interval[1], newInterval[1]);
            }
        }

        // If the new interval is not null, add it to the result list.
        if (newInterval != null) {
            res.add(newInterval);
        }

        // Return the result list as an array of intervals.
        return res.toArray(new int[res.size()][]);
    }

}
//the time complexity of the insert() method is O(n) and the space complexity is O(1)