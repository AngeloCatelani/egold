class Solution:
    def rotateString(self, A: str, B: str) -> bool:
        if not A and not B:
            return True
        if A == B:
            return True
        result = ""
        
        i = 1
        while i < len(A):            
            result = A[i:] + A[:i]
            
            if result == B:
                return True
            
            i += 1
            
            
        return False

        

        
# Time-O(n)
# Space=O(n)

