class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = set()
        l = 0
        maxL = 0

        for r in range(len(s)):
            # If the character is already in the set, remove characters from the left
            # until we remove the duplicate character
            while s[r] in char_set:
                char_set.remove(s[l])
                l += 1
            # Add the current character to the set
            char_set.add(s[r])
            # Update the maximum length
            maxL = max(maxL, r - l + 1)
        
        return maxL
