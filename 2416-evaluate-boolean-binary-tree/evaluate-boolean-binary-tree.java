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
  public boolean evaluateTree(TreeNode root) {
    if (root.val < 2)
      return root.val == 1;
    if (root.val == 2) // OR
      return evaluateTree(root.left) || evaluateTree(root.right);
    // AND
    return evaluateTree(root.left) && evaluateTree(root.right);
  }
}
// public boolean evaluateTree(TreeNode root) {

// This method takes the root node of the tree as an argument and returns a boolean.
// if (root.val < 2) return root.val == 1;

// If the value of the current node is less than 2 (either 0 or 1), the method checks if the value is equal to 1 and returns that comparison result directly.
// if (root.val == 2) // OR

// If the value of the current node is 2, it proceeds to evaluate logical OR operation on the left and right subtrees.
// return evaluateTree(root.left) || evaluateTree(root.right);

// The code recursively calls evaluateTree on the left and right subtrees and returns the logical OR of their results.
// return evaluateTree(root.left) && evaluateTree(root.right);

// If the current node's value is neither 0 nor 1 and is equal to 2, this line performs a logical AND operation on the results of evaluateTree for the left and right subtrees.