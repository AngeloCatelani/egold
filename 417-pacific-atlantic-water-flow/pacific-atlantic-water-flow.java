class Solution {
    public List<List<Integer>> pacificAtlantic(int[][] heights) {
        List<List<Integer>> res = new ArrayList<>();
        int r = heights.length;
        int c = heights[0].length;
        boolean [][] pacific = new boolean [r][c];
         boolean [][] atlantic = new boolean [r][c];
         for(int i=0;i<c;i++){
             dfs(0,i,r,c,heights,pacific,Integer.MIN_VALUE);
           dfs(r-1,i,r,c,heights,atlantic,Integer.MIN_VALUE);
         }
            for(int i=0;i<r;i++){
             dfs(i,0,r,c,heights,pacific,Integer.MIN_VALUE);
           dfs(i,c-1,r,c,heights,atlantic,Integer.MIN_VALUE);
         }
         for(int i=0;i<r;i++){
             for(int j =0;j<c;j++){
                 if(pacific[i][j] && atlantic[i][j]){
                     res.add(Arrays.asList(i,j));
                 }
             }
         }
         return res;
    }
    private void  dfs(int i,int j,int r,int c,int[][] heights, boolean [][] ocean,int prev){
        if(i<0 || j< 0 || j>=c||i>=r || ocean[i][j] || heights[i][j] < prev){
            return;
        }
        ocean[i][j] = true;
         dfs(i+1,j,r,c,heights,ocean,heights[i][j]);
               dfs(i-1,j,r,c,heights,ocean,heights[i][j]);
                     dfs(i,j+1,r,c,heights,ocean,heights[i][j]);
                           dfs(i,j-1,r,c,heights,ocean,heights[i][j]);
                        
    }
}