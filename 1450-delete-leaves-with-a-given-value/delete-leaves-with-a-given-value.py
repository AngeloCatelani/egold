# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        def dfs(node):
            if not node:
                return None
            
            # Recursively process the left and right subtrees
            node.left = dfs(node.left)
            node.right = dfs(node.right)
            
            # If the node is a leaf and its value is the target, remove it by returning None
            if not node.left and not node.right and node.val == target:
                return None
            
            return node
        
        return dfs(root)