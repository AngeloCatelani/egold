# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findTarget(self, root, k):
        """
        :type root: Optional[TreeNode]
        :type k: int
        :rtype: bool
        """
        def inorder(root, seen):
            if not root:
                return False
            
            # Check if we can find k - current value in seen set
            if k - root.val in seen:
                return True
                
            # Add current value to seen set
            seen.add(root.val)
            
            # Recursively check left and right subtrees
            return inorder(root.left, seen) or inorder(root.right, seen)
            
        return inorder(root, set())
# time and space-O(n)