# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(root):
            # If the current node is None, it is balanced and its height is 0
            if not root:
                return [True, 0]
            
            # Recursively check the left subtree
            left = dfs(root.left)
            # Recursively check the right subtree
            right = dfs(root.right)
            
            # Check if the current node is balanced:
            # - left[0] checks if the left subtree is balanced
            # - right[0] checks if the right subtree is balanced
            # - abs(left[1] - right[1]) <= 1 checks if the current node's subtrees' heights differ by no more than 1
            balanced = left[0] and right[0] and abs(left[1] - right[1]) <= 1
            
            # Return whether the current subtree is balanced and its height
            # - balanced: whether the current subtree is balanced
            # - 1 + max(left[1], right[1]): height of the current subtree
            return [balanced, 1 + max(left[1], right[1])]

        # Start the DFS from the root and return whether the entire tree is balanced
        return dfs(root)[0]
# For node 4:
# left = [True, 0]
# right = [True, 0]
# balanced = left[0] and right[0] and abs(left[1] - right[1]) <= 1
# balanced = True and True and abs(0 - 0) <= 1 which is True
# height = 1 + max(left[1], right[1])
# height = 1 + max(0, 0) which is 1
# dfs(node 4) returns [True, 1].