public class Solution {
    public static int[][] setZeroes(int[][] matrix) {
        HashSet<Integer> rowMap = new HashSet<>();
        HashSet<Integer> colMap = new HashSet<>();

        int row = matrix.length;
        int col = matrix[0].length;

        for (int i = 0; i < row; i++) {
            for (int j = 0; j < col; j++) {
                if (matrix[i][j] == 0) {
                    rowMap.add(i);
                    colMap.add(j);
                }
            }
        }

        for (int i = 0; i < row; i++) {
            for (int j = 0; j < col; j++) {
                if (rowMap.contains(i) || colMap.contains(j)) {
                    matrix[i][j] = 0;
                }
            }
        }

        return matrix;
    }
}
//he time complexity of the code is O(nm) and the space complexity is O(n + m).