class Solution {
    public int[][] merge(int[][] intervals) {
        Arrays.sort(intervals,(a,b)->Integer.compare(a[0],b[0]));
        List<int[]>output = new ArrayList<>();
        int [] curr = intervals[0];
        output.add(curr);
        for(int i =1; i <intervals.length;i++){
            if(curr[1]>=intervals[i][0]){
                curr[0] = Math.min(curr[0],intervals[i][0]);
                curr[1] = Math.max(curr[1],intervals[i][1]);
            }
            else{
                curr = intervals[i];
                output.add(curr);
            }

        }
        return output.toArray(new int [0][]);
    }
}