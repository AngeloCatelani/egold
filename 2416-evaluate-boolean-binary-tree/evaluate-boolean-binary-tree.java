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
//  Time: O(n) Space: O(h)
class Solution {
    public boolean evaluateTree(TreeNode root) {
        if(root.val==0) return false;
        else if(root.val==1) return true;
        boolean b1 = evaluateTree(root.left);
        boolean b2 = evaluateTree(root.right);
        if(root.val==2) return b1||b2;
        else return b1&&b2;
    }
}