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
    public boolean leafSimilar(TreeNode root1, TreeNode root2) {
        //get the leaf nodes in a arr and check same or not
        List<Integer> leaf1 = new ArrayList<>();
         List<Integer> leaf2 = new ArrayList<>();
leaf( root1,leaf1);
          leaf( root2,leaf2);
          return leaf1.equals(leaf2);

    }
    private void leaf(TreeNode root,List<Integer> leaves){
        if(root == null)return ;
        if(root.left == null && root.right == null){
            leaves.add(root.val);
        }
         leaf( root.left,leaves);
          leaf( root.right,leaves);
    }
}