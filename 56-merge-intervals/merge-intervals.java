import java.util.*;

public class Solution {
    public int[][] merge(int[][] intervals) {
        if (intervals.length <= 1) {
            return intervals;
        }

        // Sort the array so that earlier start times are at the beginning
        Arrays.sort(intervals, (a, b) -> Integer.compare(a[0], b[0]));

        List<int[]> output = new ArrayList<>();
        int[] current = intervals[0];
        output.add(current);

        // If the current interval's end time is greater than or equal to
        // the next interval's start time, then we know there is an overlap
        // and we merge them. If there is no overlap, then we add the next
        // interval to the list of intervals in our output array.
        for (int i = 1; i < intervals.length; i++) {
            int[] next = intervals[i];
            if (current[1] >= next[0]) {
                current[1] = Math.max(current[1], next[1]);
            } else {
                current = next;
                output.add(current);
            }
        }

        return output.toArray(new int[0][]);
    }
}
