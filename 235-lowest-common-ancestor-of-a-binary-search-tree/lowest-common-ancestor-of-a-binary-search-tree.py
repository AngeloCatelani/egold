# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # Base case: if root is None, return None
        if not root:
            return None
        
        # If the current node is either p or q, return the current node
        if root == p or root == q:
            return root
        
        # Recur for the left and right subtree
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        
        # If both left and right are non-null, it means p and q are found in
        # different subtrees, so the current node is their LCA
        if left and right:
            return root
        
        # Otherwise, return the non-null value between left and right
        return left if left else right