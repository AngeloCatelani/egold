
# // bfs
# // iterative
# //queue
# //level by level

# // Given the roots of two binary trees p and q, write a function to check if they are the same or not.

# // Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

 

# // Example 1:


# // Input: p = [1,2,3], q = [1,2,3]
# // Output: true
# // Example 2:


# // Input: p = [1,2], q = [1,null,2]
# // Output: false
# // Example 3:


# // Input: p = [1,2,1], q = [1,1,2]
# // Output: false
 

# // Constraints:

# // The number of nodes in both trees is in the range [0, 100].
# // -104 <= Node.val <= 104



def isSameTree(self, p, q):
    # both  are none(null) True
    #  either one none means False
    # values are not same False
    # Why it follows dFS???

    if not p and not q:
        return True
    if not p or not q :
        return False
    if p.val != q.val:
        return False
    return((self.isSameTree(p.right,q.right))and (self.isSameTree(p.left,q.left)))  #Otherwise, the function recursively checks if the left and right subtrees of p are the same as the left and right subtrees of q, respectively. If both of these recursive calls return True, then the function returns True, indicating that the two trees are the same. If either recursive call returns False, then the function returns False, indicating that the trees are not the same.
    #    need to use the self keyword to refer to the current object, 
    
  
#   function isSameTree(p, q) {
#     // p and q are both null
#     if (!p && !q) {
#         return true;
#     }
#     // one of p and q is null
#     if (!q || !p) {
#         return false;
#     }
#     if (p.val !== q.val) {
#         return false;
#     }
#     return isSameTree(p.right, q.right) && isSameTree(p.left, q.left);
# }

# DFS the tree
# iterative DFS on tree
# Instantiate a stack
# Put both root nodes in the stack as a pair or tuple
# Loop and continue looping until stack is empty or we return false early
# Pop the stack and compare the nodes
# Return false if either nodes don't match
# Push the nodes children as pairs onto the stack for future comparison
# Return true at the end if we make it through the whole tree


def isSameTree(self,p,q):
    queue=[]
    queue.append((p,q))
    print(queue,"queue")
    while queue:
       node1, node2 = queue.pop(0)
       if node1 and node2 and node1.val == node2.val:
          queue.append((node1.left , node2.left))
          queue.append((node1.right , node2.right))
       elif node1 or node2:
          return False
    return True


# Time Complexity: O(m+n)

# Space Complexity: O(m+n)


def sameTree(self,p,q):
    stack=[(p,q)]
    while stack:
        n, m = stack.pop(0)
        if n and m and n.val == m.val:
            stack.append((n.left,m.right))
            stack.append((n.right,m.right))
        elif n or m:
            return False

    return True
    