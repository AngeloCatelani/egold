# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode], low=float('-inf'), high=float('inf')) -> bool:
        if not root:
            return True

        val = root.val

        if val <= low or val >= high:
            return False

        if not self.isValidBST(root.left, low, val):
            return False
        if not self.isValidBST(root.right, val, high):
            return False

        return True
