# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, r1: Optional[TreeNode], r2: Optional[TreeNode]) -> Optional[TreeNode]:
        if not r1 and not r2:
            return None
        val1 = r1.val if r1 else 0
        val2 = r2.val if r2 else 0
        r3 = TreeNode(val1 + val2)
        r3.left = self.mergeTrees(r1.left if r1 else None,r2.left if r2 else None)
        r3.right = self.mergeTrees(r1.right if r1 else None,r2.right if r2 else None)
        return r3

# class Solution:
#     def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
#         if not t1 and not t2:
#             return None

#         v1 = t1.val if t1 else 0
#         v2 = t2.val if t2 else 0
#         root = TreeNode(v1 + v2)

#         root.left = self.mergeTrees(t1.left if t1 else None, t2.left if t2 else None)
#         root.right = self.mergeTrees(t1.right if t1 else None, t2.right if t2 else None)
#         return root
       
        