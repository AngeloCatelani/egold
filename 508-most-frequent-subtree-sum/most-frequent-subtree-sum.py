# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:
        count = Counter()
        if not root:
            return []
        def dfs(root):
            if not root:
                return 0
            left =dfs(root.left)
            right = dfs(root.right)
            sumL = left + right+ root.val
            count[sumL]+=1
            return sumL

        dfs(root)
        maxL = max(count.values())
        return [ s for s in count if count[s] == maxL]