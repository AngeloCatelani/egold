def mergeTrees(self, t1: Optional[TreeNode], t2: Optional[TreeNode]) -> Optional[TreeNode]:
      def mergeTrees(self, t1: Optional[TreeNode], t2: Optional[TreeNode]) -> Optional[TreeNode]:
        # initialize new tree
        # root of new tree = root1.val+ root2.val
        # left = root1.left.val+ root2.left.val
        # right = root1.right.val+ root2.right.val
        # if it has left or right just add to the new tree nodes
        if not t1 and not  t2:  # if both of null return none
            return None
        
        v1 = t1.val if t1 else 0   # if there is value take that else take 0 as val
        v2 = t2.val if t2 else 0    # if there is value take that else take 0 as val

        root = TreeNode(v1+v2)

        root.left = (self.mergeTrees(t1.left if t1 else None ,t2.left if t2 else None )  ) # left node may or may not be present. If not present take none as value
        root.right = (self.mergeTrees(t1.right if t1 else None ,t2.right if t2 else None )  )

        return root

        # time - O(n)