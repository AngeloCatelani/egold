# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        small , prev = float("inf") , None
        if not root:
            return
        def inorder(root):
            nonlocal small,prev
            if not root:
                return
            inorder(root.left)
            if prev is not None:
                small = min(small,root.val - prev.val)
            prev = root
            inorder(root.right)
        
        inorder(root)
        return small