class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # Dictionary to store the frequency of each character in the magazine
        char_count = {}
        
        # Count each character in the magazine
        for char in magazine:
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
        
        # Check if the ransomNote can be constructed
        for char in ransomNote:
            if char in char_count and char_count[char] > 0:
                char_count[char] -= 1
            else:
                return False
        
        return True