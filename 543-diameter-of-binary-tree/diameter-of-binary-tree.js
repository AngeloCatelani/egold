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
var diameterOfBinaryTree = function(root) {
    let diameter = 0;

    const height = (node) => {
        if (!node) return 0;

        const leftHeight = height(node.left);
        const rightHeight = height(node.right);

        // Update the diameter at this node
        diameter = Math.max(diameter, leftHeight + rightHeight);

        // Return the height of this node
        return 1 + Math.max(leftHeight, rightHeight);
    };

    height(root);
    return diameter;
};