# class TreeNode:
#     def __init__(val,left=None,right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        # recursive
        # not root return none
        # if val < root.val search left side of tree
        # if val > root.val search in right side of tree
        # else return root

        if not root:
            return None
        while root:
            if val < root.val:
                return self.searchBST(root.left,val)
            elif val > root.val:
                return self.searchBST(root.right,val)
            else:
                return root

        
        