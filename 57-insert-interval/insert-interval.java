class Solution {
    public int[][] insert(int[][] intervals, int[] newInterval) {
        
        int n = intervals.length;
        List<int[]> res = new ArrayList();
        boolean intervalInserted = false;

        for(int i=0;i<n;i++) {
            if(intervals[i][1] < newInterval[0]) {
                res.add(intervals[i]);
            } else if(intervals[i][0] > newInterval[1]) {
                if(!intervalInserted) {
                    res.add(newInterval);
                    intervalInserted = true;
                }
                res.add(intervals[i]);
            } else {
                newInterval[0] = Math.min(newInterval[0], intervals[i][0]);
                newInterval[1] = Math.max(newInterval[1], intervals[i][1]);
            }
        }

        if(!intervalInserted) {
            res.add(newInterval);
        }

        return res.toArray(new int[0][]); // convert to 2D array
    }
}
// Time Complexity: O(n)

// Space Complexity: O(n)
// Loop through the intervals:

// Iteration 0: intervals[i] = [1,2], newInterval = [4,8].
// Since intervals[i][1] (2) is less than newInterval[0] (4), intervals[i] is added to res.
// Iteration 1: intervals[i] = [3,5], newInterval = [4,8].
// The intervals overlap, so the new interval is merged with intervals[i].
// newInterval becomes [3,8].
// Iteration 2: intervals[i] = [6,7], newInterval = [3,8].
// The intervals do not overlap, so intervals[i] is added to res.
// Iteration 3: intervals[i] = [8,10], newInterval = [3,8].
// The intervals overlap, so the new interval is merged with intervals[i].
// newInterval becomes [3,10].
// Iteration 4: intervals[i] = [12,16], newInterval = [3,10].
// The intervals do not overlap, so intervals[i] is added to res.
// After the loop, check if the newInterval was inserted:

// Since intervalInserted is false, insert the newInterval into res.
// Convert the res ArrayList to a 2D array and return it as the result.