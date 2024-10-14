class Solution:
    def isSymmetric(self, root) :
        if not root:
            return True
        stack=[(root.left,root.right)]
        while stack:
            n, m = stack.pop(0)
            if n and m and n.val == m.val:
                stack.append((n.left,m.right))
                stack.append((n.right,m.left))
            elif n or m:
                return False
        return True

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# def isSymmetric(root: TreeNode) -> bool:
#     if not root:
#         return True

#     stack = [(root.left, root.right)]
#     while stack:
#         left, right = stack.pop()
#         if not left and not right:
#             continue
#         if not left or not right or left.val != right.val:
#             return False
#         stack.append((left.left, right.right))
#         stack.append((left.right, right.left))

#     return True
# This solution uses an iterative approach, utilizing a stack to keep 
# track of the nodes to be processed. It starts by pushing the left and 
# right children of the root node onto the stack. It then processes the nodes in pairs, 
# popping the top two nodes from the stack and comparing their values. If the values are not equal, 
# the function returns False. Otherwise, it pushes the left and right children of the first node and 
# the right and left children of the second node onto the stack, respectively. This ensures that the nodes 
# are processed in a way that reflects the symmetry of the tree. The function continues this process until 
# the stack is empty, at which point it returns True.