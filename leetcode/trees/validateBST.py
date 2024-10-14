# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # left node < root 
        # right node > root 
       
        def isValid(node,left,right): # two boundaries means -infinity to +infinity
          if not node:  # null node is true
              return True
        
              
          if  not (node.val < right and node.val > left): # if left and right do not satisfy the conditions
              return False
          return (isValid(node.left,left,node.val) and isValid(node.right,node.val,right)) 
        #   left side between -inf > node.left < node.val and node.right > node.val but less than inf
        return isValid(root,float("-inf"),float("+inf"))
