# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(root,sumL):
            if not root:
                return False
            sumL += root.val
            if not root.left and not root.right and  sumL == targetSum:
                return True
            return dfs(root.left,sumL) or dfs(root.right,sumL)
            
        


        return dfs(root,0)

        