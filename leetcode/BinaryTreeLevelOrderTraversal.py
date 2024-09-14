# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result=[] # initialize empty list
        queue=[root] # append root into queue
        print(queue,"queue")
        while len(queue)  > 0: # queue length > 0
            length = len(queue) # goes level by level
            level=[] # inner list
            for i in range(length): # range(0,length) starts with 0 and stops at given second element
              node = queue.pop(0)
              if node: 
                level.append(node.val) 
                if node.left : # if node is true and it has left
                    queue.append(node.left) 
                if node.right:
                    queue.append(node.right) 
            if len(level) > 0:
                result.append(level)
        return result
            