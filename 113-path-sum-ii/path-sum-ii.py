# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        path = []
        outer = []
        total = 0
        def dfs(root,sum):
            nonlocal total,path,outer
            if not root:
                return
            total += root.val
            path.append(root.val)
            if root.left is None  and root.right is None and total == sum:
                outer.append(path[:])
            dfs(root.left,sum)
            dfs(root.right,sum)
            total -= root.val
            path.pop()

        dfs(root,targetSum)
       

        return outer