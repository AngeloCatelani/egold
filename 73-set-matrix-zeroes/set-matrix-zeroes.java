class Solution {
    public void setZeroes(int[][] matrix) {
        int R =  matrix.length;
        int C = matrix[0].length;
        HashSet<Integer> rSet = new HashSet<>();
         HashSet<Integer> cSet = new HashSet<>();
         for(int i=0;i<R;i++){
             for(int j=0;j<C; j++){
                 if(matrix[i][j] == 0){
                     rSet.add(i);
                     cSet.add(j);
                 }
             }
         }
          for(int i=0;i<R;i++){
             for(int j=0;j<C; j++){
                 if(rSet.contains(i) || cSet.contains(j)){
                     matrix[i][j] =0;
                 }
             }}
    }
}