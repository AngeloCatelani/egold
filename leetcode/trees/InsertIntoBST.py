def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        curr = root
        if not curr:
            return TreeNode(val)
        if val > curr.val:
            curr.right = self.insertIntoBST(curr.right,val)
        if val< curr.val:
            curr.left = self.insertIntoBST(curr.left,val)
        return curr