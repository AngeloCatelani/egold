# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        
        def dfs(node, current_sum):
            nonlocal count
            if not node:
                return

            # Update the current sum
            current_sum += node.val

            # Check if there's a sub-path (ending at this node) that sums to targetSum
            count += prefix_sums[current_sum - targetSum]

            # Update the prefix sums with the current sum
            prefix_sums[current_sum] += 1

            # Recurse on left and right children
            dfs(node.left, current_sum)
            dfs(node.right, current_sum)

            # Restore the prefix sums as we go back to the parent node
            prefix_sums[current_sum] -= 1

        count = 0
        prefix_sums = defaultdict(int)
        prefix_sums[0] = 1  # Base case to handle if the node's value equals targetSum

        dfs(root, 0)

        return count