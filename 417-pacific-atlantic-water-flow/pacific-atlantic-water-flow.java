class Solution {
  int[][] dir = { { 0, 1 }, { 0, -1 }, { 1, 0 }, { -1, 0 } };

  public List<List<Integer>> pacificAtlantic(int[][] heights) {
    List<List<Integer>> res = new ArrayList<>();
    int rows = heights.length;
    int cols = heights[0].length;
    boolean[][] pacific = new boolean[rows][cols];
    boolean[][] atlantic = new boolean[rows][cols];

    // Loop to start DFS from the Pacific coast
    for (int i = 0; i < cols; i++) {
      dfs(heights, 0, i, Integer.MIN_VALUE, pacific);
    }

    // Loop to start DFS from the Atlantic coast
    for (int i = 0; i < cols; i++) {
      dfs(heights, rows - 1, i, Integer.MIN_VALUE, atlantic);
    }

    // Loop to start DFS from the left and right boundaries
    for (int i = 0; i < rows; i++) {
      dfs(heights, i, 0, Integer.MIN_VALUE, pacific);
      dfs(heights, i, cols - 1, Integer.MIN_VALUE, atlantic);
    }

    // Check cells that can reach both the Pacific and Atlantic
    for (int i = 0; i < rows; i++) {
      for (int j = 0; j < cols; j++) {
        if (pacific[i][j] && atlantic[i][j]) {
          res.add(Arrays.asList(i, j));
        }
      }
    }
    return res;
  }

  private boolean dfs(int[][] heights, int i, int j, int prev, boolean[][] ocean) {
    if (i < 0 || i >= ocean.length || j < 0 || j >= ocean[0].length)
      return false;

    if (heights[i][j] < prev || ocean[i][j])
      return false;

    ocean[i][j] = true;

    // Explore in all four directions
    for (int[] d : dir) {
      dfs(heights, i + d[0], j + d[1], heights[i][j], ocean);
    }

    return true;
  }
}
