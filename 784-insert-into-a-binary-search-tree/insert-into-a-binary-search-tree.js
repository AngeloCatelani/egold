/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @param {number} val
 * @return {TreeNode}
 */
var insertIntoBST = function(root, val) {
     // Base case: if root is null, create and return a new node
    if (root === null) {
        return new TreeNode(val);
    }

    // If val is less than root's value, insert into left subtree
    if (val < root.val) {
        root.left = insertIntoBST(root.left, val);
    }
    // If val is greater than root's value, insert into right subtree
    else {
        root.right = insertIntoBST(root.right, val);
    }

    return root; // Return the unchanged root pointer
};