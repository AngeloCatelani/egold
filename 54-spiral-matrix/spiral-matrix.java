class Solution {

    public List<Integer> spiralOrder(int[][] matrix) {

        // Declare a list to store the result of the algorithm.
        List<Integer> list = new ArrayList<>();

        // Initialize four variables to track the row and column boundaries.
        int rb = 0; // row begin
        int re = matrix.length - 1; // row end
        int cb = 0; // column begin
        int ce = matrix[0].length - 1; // column end

        // Iterate while there are still rows and columns to be traversed.
        while (rb <= re && cb <= ce) {

            // **Line-by-line explanation:**
            // * This while loop will iterate while the row begin index is less than or equal to the row end index and the column begin index is less than or equal to the column end index. In other words, the loop will iterate while there are still rows and columns to be traversed.

            // Traverse the top row of the matrix from left to right.
            for (int j = cb; j <= ce; j++) {
                list.add(matrix[rb][j]);
            }

            // **Line-by-line explanation:**
            // * This for loop traverses the top row of the matrix from left to right, adding each element to the list.

            // Increment the row begin index.
            rb++;

            // **Line-by-line explanation:**
            // * This line increments the row begin index by 1, so that the next iteration of the while loop will traverse the next row.

            // Traverse the rightmost column of the matrix from top to bottom.
            for (int i = rb; i <= re; i++) {
                list.add(matrix[i][ce]);
            }

            // **Line-by-line explanation:**
            // * This for loop traverses the rightmost column of the matrix from top to bottom, adding each element to the list.

            // Decrement the column end index.
            ce--;

            // **Line-by-line explanation:**
            // * This line decrements the column end index by 1, so that the next iteration of the while loop will traverse the previous column.

            // Check if the row begin index is less than or equal to the row end index.
            if (rb <= re) {

                // Traverse the bottom row of the matrix from right to left.
                for (int j = ce; j >= cb; j--) {
                    list.add(matrix[re][j]);
                }

                // **Line-by-line explanation:**
                // * This if statement checks if the row begin index is less than or equal to the row end index. If it is, then the for loop inside the if statement will traverse the bottom row of the matrix from right to left, adding each element to the list.

            }

            // Decrement the row end index.
            re--;

            // **Line-by-line explanation:**
            // * This line decrements the row end index by 1, so that the next iteration of the while loop will traverse the previous row.

            // Check if the column begin index is less than or equal to the column end index.
            if (cb <= ce) {

                // Traverse the leftmost column of the matrix from bottom to top.
                for (int i = re; i >= rb; i--) {
                    list.add(matrix[i][cb]);
                }

                // **Line-by-line explanation:**
                // * This if statement checks if the column begin index is less than or equal to the column end index. If it is, then the for loop inside the if statement will traverse the leftmost column of the matrix from bottom to top, adding each element to the list.

            }

            // Increment the column begin index.
            cb++;

            // **Line-by-line explanation:**
            // * This line increments the column begin index by 1, so that the next iteration of the while loop will traverse the next column.

        }

        // Return the list of elements in spiral order.
        return list;

    }

}

