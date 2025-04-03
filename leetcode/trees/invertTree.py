# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def invertTree(self,  root: Optional[TreeNode]) -> Optional[TreeNode] :
              
          if not root:
              return
          stack = [root] # pasting whole tree itself
          while stack:
              node = stack.pop(0)
              print(node)
              node.left,node.right = node.right,node.left
              if node.left:
                  stack.append(node.left)
              if node.right:
                  stack.append(node.right)
          return root
     

a = Solution()
a.invertTree([2,1,3])
     # ##########################swap-dfs####################################
        # if not root:
        #     return None
        
        # temp = root.left
        # root.left = root.right
        # root.right = temp

        # self.invertTree(root.left)
        # self.invertTree(root.right)

        # return root
 # ##########################swap-dfs -iterative####################################
        # stack = []

        # if not root:
        #     return None
        # stack.append(root)

        # while stack:
        #     node = stack.pop()
        #     node.left ,node.right = node.right,node.left

        #     if node.left:
        #         self.invertTree(node.left)
        #     if node.right:
        #         self.invertTree(node.right)
        # return root
 # ##########################swap-bfs####################################
        queue = []

        if not root:
            return None
        queue.append(root)

        while queue:
            node = queue.pop()
            node.left ,node.right = node.right,node.left

            if node.left:
                self.invertTree(node.left)
            if node.right:
                self.invertTree(node.right)
        return root



        
        