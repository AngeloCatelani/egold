class Solution {
    public int numIslands(char[][] grid) {
        int r = grid.length;
        int c = grid[0].length;
        int count = 0;
        HashSet<Integer> set = new HashSet<>();
        for (int i = 0; i < r; i++) {
            for (int j = 0; j < c; j++) {
                if (grid[i][j] == '1') {
                    if (dfs(i, j, r, c, set, grid)) {
                        count++;
                    }
                }
            }
        }
        return count;
    }

    private boolean dfs(int i, int j, int r, int c, HashSet<Integer> set, char[][] grid) {
        if (i >= r || j >= c || i < 0 || j < 0 || set.contains(i * c + j) || grid[i][j] == '0') {
            return false;
        }
        set.add(i * c + j);
        dfs(i + 1, j, r, c, set, grid);
        dfs(i - 1, j, r, c, set, grid);
        dfs(i, j + 1, r, c, set, grid);
        dfs(i, j - 1, r, c, set, grid);
        return true;
    }
}
