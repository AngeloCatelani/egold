/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {

    public int maxPathSum(TreeNode root) {
        // Initialize the result to the lowest possible value.
        int[] res = { Integer.MIN_VALUE };

        // Recursively find the maximum path sum for the given root node.
        dfs(root, res);

        // Return the maximum path sum.
        return res[0];
    }

    /**
     * Recursively finds the maximum path sum for the given root node.
     *
     * @param root The root node of the subtree.
     * @param res An array to store the maximum path sum so far.
     * @return The maximum path sum for the given root node.
     */
    public int dfs(TreeNode root, int[] res) {
        // If the root node is null, then the maximum path sum is 0.
        if (root == null) {
            return 0;
        }

        // Recursively find the maximum path sum for the left and right subtrees.
        int left = Math.max(0, dfs(root.left, res));
        //the 0 is used as a boundary or threshold value to ensure that negative values are not included in the calculation of the left variable. 
        int right = Math.max(0, dfs(root.right, res));

        // Update the result variable with the maximum path sum that goes through the current node.(with split into left and right)
        res[0] = Math.max(res[0], root.val + left + right);

        // Return the maximum path sum that starts from the current node and goes down to one of its children.(without split)
        return root.val + Math.max(left, right);
    }
}
//time =O(n) space =O(h)h=height of tree