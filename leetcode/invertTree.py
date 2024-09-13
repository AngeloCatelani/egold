# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def invertTree(self,  root: Optional[TreeNode]) -> Optional[TreeNode] :
              
          if not root:
              return
          stack = [root] # pasting whole tree itself
          while stack:
              node = stack.pop(0)
              print(node)
              node.left,node.right = node.right,node.left
              if node.left:
                  stack.append(node.left)
              if node.right:
                  stack.append(node.right)
          return root
     

a = Solution()
a.invertTree([2,1,3])
    