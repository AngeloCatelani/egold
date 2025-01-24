def isBalanced( root) :
    # return boolean
    def dfs(node):
        if not node:
            return [True,0]
        left = dfs(node.left)
        right = dfs(node.right)
        balanced = left[0] and right[0] and (abs(left[1] - right[1]))
        return balanced,1+max(left[1] , right[1])
    return dfs(root)[0]

        # def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # def bst(node):
        #     if not node:
        #         return [True,0]
        #     left = bst(node.left)
        #     right = bst(node.right)
        #     balanced = left[0] and right[0] and (abs((left[1]-right[1]))) <=1
        #     return balanced,1+max(left[1],right[1])

        # return bst(root)[0]
            
print(isBalanced([1,2,2,3,3,null,null,4,4]))