# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
  
        # Initialize a variable to keep track of the maximum diameter found
        res = 0

        # Define a helper function for depth-first search
        def dfs(root):
            nonlocal res  # Allows modification of the 'res' variable in the outer scope

            if not root:  # If the current node is None, return 0 (base case)
                return 0
            
            # Recursively find the height of the left subtree
            left = dfs(root.left)
            # Recursively find the height of the right subtree
            right = dfs(root.right)
            
            # Update the maximum diameter found so far
            # Diameter at the current node is left height + right height
            res = max(res, left + right)
            
            # Return the height of the current node
            # Height is 1 (for the current node) plus the maximum of left and right subtree heights
            return 1 + max(left, right)

        # Start the depth-first search from the root
        dfs(root)
        # Return the maximum diameter found
        return res

# Example to demonstrate the algorithm:
# Let's consider the following binary tree:
#      1
#     / \
#    2   3
#   / \
#  4   5
#
# The diameter of this tree is 3 (path 4 -> 2 -> 1 -> 3 or path 5 -> 2 -> 1 -> 3).
