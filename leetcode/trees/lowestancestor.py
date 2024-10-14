# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        curr = root
        while curr:
            if p.val > curr.val and q.val > curr.val:# both p and q are greater than root.val search right side of bst
                curr = curr.right
            elif p.val < curr.val and q.val < curr.val: # both p and q are lesser than root.val search left side of bst
                curr = curr.left
           
            else : 
                # print(curr,"curr")
                return curr