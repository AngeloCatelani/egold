class Solution:
    def countGoodSubstrings(self, s: str) -> int:
    
        # Check if the length of the string is less than 3
        if len(s) < 3:
            return 0
        
        count = 0
        for i in range(len(s) - 2):
            substring = s[i:i+3]
            if len(set(substring)) == 3:  # Check if all characters in the substring are unique
                count += 1
        
        return count



