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
// class Solution {
//     public TreeNode searchBST(TreeNode root, int val) {
//         if(root == null)return null;
//         TreeNode left = searchBST(root.left, val);
//         TreeNode right = searchBST(root.right, val);
//         if(val == left.val)return left;
//         if(val == right.val) return right;

//         // if(val < root.val){
//         //     //search left side
//         // }
//         // else{
//         //     //search right side
//         // }
//     }
// }
class Solution {
    public TreeNode searchBST(TreeNode root, int val) {
        if (root == null) return null;

        if (root.val == val) {
            return root; // Found the node with the desired value
        } else if (val < root.val) {
            return searchBST(root.left, val); // Search in the left subtree
        } else {
            return searchBST(root.right, val); // Search in the right subtree
        }
    }
}
