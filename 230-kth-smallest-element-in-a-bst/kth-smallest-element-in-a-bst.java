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
    public int kthSmallest(TreeNode root, int k) {
        //want to sort the tree nodes so that smallest elemt in tree can match k
        //so going to use inorder tree traversal
        //using a stack to store elements
        // first add root to stack then proceed to left add left node to stack and proceed further
        //once it reaches null to all its child. pop the node from stack as it is visited and go to right nodes
        // eg stack = [5]->topview
        //then go to left 3 add 3 to stack [5,3]
        // go to left 2 add 2 to stack [5,3,2]
        // then go to left 1 add 1 to stack[5,3,2,1]
        //since 1 doe not have any child pop 1 from stack since it is visited so stack will be [5,3,2]and visited = [1]then go to 2 does not have right child pop 2 from stack
        // visited =[1,2,] and stack is [5,3]
        //then curr is at 3 which has right so pop 3 from stack and add it right child to stack  visited =[1,2,3] and stack is [5,4]
        // then go to 4 does not have right child pop 4 from stack. visited =[1,2,3,4] and stack is [5,]
        // then curr is at root which has right child so pop 5 from stack and right child 6 visited =[1,2,3,4,5] and stack is [6] and 6 does not not have any child pop it out and stack is empty end of func visited =[1,2,3,4,5,6] and stack is [] 

        int  n = 0;
        Stack<TreeNode>stack = new Stack<>();
        TreeNode curr = root;
        while(curr != null || !stack.isEmpty()){
           while(curr != null){
               stack.push(curr);
               curr = curr.left;
           }
            n++;
           curr = stack.pop();
          
           if(n == k){
               return curr.val;
           }
         curr = curr.right;
        }
        return -1;
    }
}