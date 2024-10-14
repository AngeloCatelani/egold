class Solution:
    def isSubtree(self, s,t) -> bool:
        if not t:   # if t is null it is a subtree of s
            return True  
        if not s:  # if s is null and t have nodes in it then it is false(s is not a subtree of t)
            return False
        if self.sameTree(s,t): # if nodes of s and t are same then return True
            return True
        return ((self.isSubtree(s.left,t))or (self.isSubtree(s.right,t)) ) # not same means go for the next node like left or right

    def sameTree(self,s,t):
        if not s and not t: # both are none return true
            return True
        if not s or not t: # anyone none return fasle
            return False
        if s and t and s.val == t.val: # both are true and their values are same go for their right and left nodes
            return((self.sameTree(s.left, t.left))and
                   (self.sameTree(s.right, t.right)))

# time complexity-visit all nodes of s and t so (s*t)