class Solution {
    public List<List<Integer>> pacificAtlantic(int[][] heights) {
        List<List<Integer>> res = new ArrayList<>();
        int r = heights.length;
        int c = heights[0].length;
        boolean[][] pacific = new boolean[r][c];
        boolean[][] atlantic = new boolean[r][c];

        for (int i = 0; i < c; i++) {
            dfs(0, i, pacific, heights, Integer.MIN_VALUE, r, c);
            dfs(r - 1, i, atlantic, heights, Integer.MIN_VALUE, r, c);
        }
        for (int i = 0; i < r; i++) {
            dfs(i, 0, pacific, heights, Integer.MIN_VALUE, r, c);
            dfs(i, c - 1, atlantic, heights, Integer.MIN_VALUE, r, c);
        }
        for (int i = 0; i < r; i++) {
            for (int j = 0; j < c; j++) {
                if (pacific[i][j] && atlantic[i][j]) {
                    res.add(Arrays.asList(i, j));
                }
            }
        }
        return res;
    }

    private void dfs(int i, int j, boolean[][] ocean, int[][] heights, int prev, int r, int c) {
        if (i < 0 || j < 0 || i >= r || j >= c || ocean[i][j] || heights[i][j] < prev) {
            return;
        }
        ocean[i][j] = true;

        dfs(i + 1, j, ocean, heights, heights[i][j], r, c);
        dfs(i - 1, j, ocean, heights, heights[i][j], r, c);
        dfs(i, j + 1, ocean, heights, heights[i][j], r, c);
        dfs(i, j - 1, ocean, heights, heights[i][j], r, c);
    }
}
