# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root) :
        if not root:
            return 0
        depth=0
        stack = [(root,1)] #start with root and level 1
        while stack:
            node,level = stack.pop(0) # why node and level can not be i separate line with same values
            print(node,"node",level,"level") 
            depth = max(depth,level)
            print(depth,"depth")
            if node.left:
                stack.append((node.left , level+1))
            if node.right:
                stack.append((node.right , level+1))
        return depth

# # Definition for a binary tree node.
# # class TreeNode:
# #     def __init__(self, val=0, left=None, right=None):
# #         self.val = val
# #         self.left = left
# #         self.right = right

# def maxDepth(root: TreeNode) -> int:
#     if not root:
#         return 0

#     return max(maxDepth(root.left), maxDepth(root.right)) + 1