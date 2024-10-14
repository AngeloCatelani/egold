class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        n = 0
        stack = []
        curr = root

        while curr or stack: # either one is true
            while curr:
                stack.append(curr)
                curr = curr.left
            
            curr = stack.pop()
            n += 1
            if n == k:
                return curr.val
            curr = curr.right