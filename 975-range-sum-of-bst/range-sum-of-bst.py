# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        total = 0
        def dfs(root):
            nonlocal total  # Declare total as nonlocal
            if not root:
                return 0
            left =dfs(root.left)
            right = dfs(root.right)

            if root.val >=low and root.val<= high:
                total += root.val



        dfs(root)
        return total
        