/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
class Solution {
    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
        if (root == null) {
            return null; // Base case: If the root is null, return null.
        }

        // Check if the current root is one of the target nodes (p or q)
        if (root == p || root == q) {
            return root; // Return the current root if it's p or q.
        }

        // Recursively search in the left and right subtrees
        TreeNode leftLCA = lowestCommonAncestor(root.left, p, q);
        TreeNode rightLCA = lowestCommonAncestor(root.right, p, q);

        // If both leftLCA and rightLCA are not null, it means p and q are found in
        // separate subtrees, so the current root is their lowest common ancestor.
        if (leftLCA != null && rightLCA != null) {
            return root;
        }

        // If only one of leftLCA or rightLCA is not null, return the non-null one
        // (the lowest common ancestor is found in one of the subtrees).
        return (leftLCA != null) ? leftLCA : rightLCA;
    }
}
