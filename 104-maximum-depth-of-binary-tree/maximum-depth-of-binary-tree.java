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
    public int maxDepth(TreeNode root) {
        Queue<TreeNode>q = new LinkedList<>();
        List<List<Integer>> outerArr = new ArrayList<>();
        if(root == null)return 0;
        q.offer(root);
        while(!q.isEmpty()){
            List<Integer>innerArr = new ArrayList<>();
            int size = q.size();
            for(int i=0;i< size;i++){
                TreeNode n= q.poll();
                innerArr.add(n.val);
                if(n.left != null){
                    q.offer(n.left);
                }
                if(n.right != null){
                    q.offer(n.right);
                }
  
            }
            outerArr.add(innerArr);
        }
        return outerArr.size();
    }
}