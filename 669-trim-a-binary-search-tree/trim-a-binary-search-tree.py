# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        def dfs(node):
            if not node:
                return None
            
            # Recursively trim the left and right subtrees
            node.left = dfs(node.left)
            node.right = dfs(node.right)
            
            # If the current node's value is less than low, the entire left subtree is not needed
            if node.val < low:
                return node.right
            
            # If the current node's value is greater than high, the entire right subtree is not needed
            if node.val > high:
                return node.left
            
            # If the current node is within range, return the node
            return node
        
        return dfs(root)
        

        