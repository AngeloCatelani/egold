class Solution {
    public int equalPairs(int[][] grid) {
        int r = grid.length;
        int c =grid[0].length;
        int ans =0;
        for(int i=0;i<r;i++){
            for(int j=0;j<c;j++){
                int k = 0;
                for(;k<grid.length;k++){
                    if(grid[i][k] != grid[k][j]){
                        break;
                    }
                }
                if(k==grid.length){
                    ans++;
                }
            }
        }
        return ans;
    }
}