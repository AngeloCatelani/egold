class Solution {
    public int[][] insert(int[][] intervals, int[] newInterval) {
        int n = intervals.length;
        List<int []>res = new ArrayList<>();
        boolean insertedInterval  = false;
        for(int i=0;i<n;i++){
            if(intervals[i][1] < newInterval[0]){
                res.add(intervals[i]);
            }
            else if(intervals[i][0] > newInterval[1]){
                if(!insertedInterval){
                    res.add(newInterval);
                    insertedInterval= true;
                }
                res.add(intervals[i]);
            }
            else{
                newInterval[0] = Math.min(intervals[i][0],newInterval[0]);
                newInterval[1] = Math.max(intervals[i][1],newInterval[1]);
            }
        }
        if(!insertedInterval){
                    res.add(newInterval);
                   
                }
                return res.toArray(new int [0][]);
    }
}