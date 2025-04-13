def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
    # recursive

    res =[]
    def helper(root):
        if not root:
            return None
        helper(root.left)
        res.append(root.val)
        helper(root.right)


    helper(root)
    return res


#    iterative
        res =[]
        stack =[]
        curr =root
        while stack or curr:
            while curr:
                stack.append(curr) #[1]
                curr = curr.left     #null
            curr = stack.pop()  
            res.append(curr.val)
            curr  = curr.right
        return res