# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        outerArr = []
        if not root:
            return root
        q = deque()
        q.append(root)

        while q:
            innerArr = []
            for i in range(len(q)):
                n = q.popleft()
                innerArr.append(n.val)
                if n.left:
                    q.append(n.left)
                if n.right:
                    q.append(n.right)
            outerArr.append(innerArr)
        return outerArr