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
 * @return {number}
 */
var diameterOfBinaryTree = function (root) {
    let diameter = 0;
    const height = (root) => {
        if (!root) return 0;
        let leftH = height(root.left);
        let rightH = height(root.right);
        diameter = Math.max(diameter,leftH+rightH);
        return 1+Math.max(leftH,rightH)
    }


    height(root)
    return diameter
};