# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        res = []
        hashmap = {}
        visited =set()

        def parent(node,parentV):
            if node:
                hashmap[node] = parentV
                parent(node.left,node)
                parent(node.right,node)
        
        def dfs(target,k):
            if not target or target.val in visited:
                return
            if k==0:
                res.append(target.val)
            visited.add(target.val)
            dfs(target.left,k-1)
            dfs(target.right,k-1)
            parent_node = hashmap.get(target)
            if parent_node:
                dfs(parent_node, k - 1)


        
        parent(root,None)
        dfs(target,k)
        return res