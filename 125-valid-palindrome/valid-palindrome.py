class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1
        
        while l < r:
            # Move left pointer to the right if not alphanumeric
            while l < r and not s[l].isalnum():
                l += 1
            # Move right pointer to the left if not alphanumeric
            while l < r and not s[r].isalnum():
                r -= 1
            # Check if characters at both pointers are equal (case insensitive)
            if s[l].lower() != s[r].lower():
                return False
            # Move pointers inward
            l += 1
            r -= 1
        
        return True