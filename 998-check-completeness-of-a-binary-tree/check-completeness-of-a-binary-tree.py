# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        q = deque([root])
        while q:
            for i in range(len(q)):
                n = q.popleft()
                if n:
                    q.append(n.left)
                    q.append(n.right)
                else:
                    while q:
                        n = q.popleft()
                        if n:
                            return False
                    return True
            