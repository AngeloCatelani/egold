# Given a binary tree, return the vertical order traversal of its nodes’ values. (ie, from top to bottom, column by column).

# If two nodes are in the same row and column, the order should be from left to right.

# Examples 1:

# Input: [3,9,20,null,null,15,7]
#    3
#   /\
#  /  \
#  9  20
#     /\
#    /  \
#   15   7 
# Output:
# [
#   [9],
#   [3,15],
#   [20],
#   [7]
# ]
# Examples 2:

# Input: [3,9,8,4,0,1,7]
#      3
#     /\
#    /  \
#    9   8
#   /\  /\
#  /  \/  \
#  4  01   7 
# Output:
# [
#   [4],
#   [9],
#   [3,0,1],
#   [8],
#   [7]
# ]
# Examples 3:

# Input: [3,9,8,4,0,1,7,null,null,null,2,5] (0's right child is 2 and 1's left child is 5)
#      3
#     /\
#    /  \
#    9   8
#   /\  /\
#  /  \/  \
#  4  01   7
#     /\
#    /  \
#    5   2
# Output:
# [
#   [4],
#   [9,5],
#   [3,0,1],
#   [8,2],
#   [7]
# ]
import collections
def verticalOrder(self, root: TreeNode):
    res =[]
    obj = collections.defaultdict(list) #{}
    queue = collections.deque([(0,root)])
    minX = float("inf")
    maxX = float("-inf")
    if not root:
        return []
    while queue:
        x,node = queue.popleft()
        obj[x].append(node.val)
        minX = min(minX,x)
        maxX = max(maxX,x)

        if node.left:
            queue.append(x-1,node.left)
        if node.right:
            queue.append(x+1,node.right)

        for level in range(minX,maxX+1):
            res.append(obj[level])
        return res

        # time O(n)
        # space O(n)
# obj={
# 0:[4,3]
# -1:[2]
# 1:[7]
# }










def verticalOrder(root):
    output =[]
    minX = float("inf")
    maxX = float("-inf")
    queue = collections.deque([0,root])
    obj = collections.defaultdict(list)

    if not root:
        return []
    
    while queue:
        x, node = queue.popleft()
        obj[x].append(node.val)
        minX = min(x,minX)
        maxX = max(x,maxX)

        if node.left:
            queue.append([x-1,node.left])
        if node.right:
            queue.append([x+1,node.right])
        
        for level in range(minX,maxX+1):
            output.append(obj[level])
        return output
        





