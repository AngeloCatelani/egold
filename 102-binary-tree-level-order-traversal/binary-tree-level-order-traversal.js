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
 * @return {number[][]}
 */
var levelOrder = function (root) {
    if (!root) return [];
    let outer = []
    let queue = [root]
    while (queue.length > 0) {
        let inner = []
        let levelSize = queue.length;
        for (let i = 0; i < levelSize; i++) {
            let node = queue.shift()
            inner.push(node.val)
            if (node.left) queue.push(node.left)
            if (node.right) queue.push(node.right)
        }
        outer.push(inner)
    }
    return outer
};