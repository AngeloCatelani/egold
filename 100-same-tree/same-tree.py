# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # If both trees are None, they are the same
        if not p and not q:
            return True
        # If one of the trees is None, they are not the same
        if not p or not q:
            return False
        # If the values of the current nodes do not match, they are not the same
        if p.val != q.val:
            return False
        # Check recursively if the left and right subtrees are the same
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
            
        
        