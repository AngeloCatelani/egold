class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        res = []  # Initialize the result list to store starting indices of anagrams
        l = 0  # Initialize the left pointer of the sliding window
        
        pMap = {}  # Dictionary to store the frequency of characters in p
        sMap = {}  # Dictionary to store the frequency of characters in the current window of s

        # Populate pMap with the frequency of each character in p
        for char in p:
            pMap[char] = 1 + pMap.get(char, 0)
        
        # Iterate over the string s
        for i in range(len(s)):
            sMap[s[i]] = 1 + sMap.get(s[i], 0)  # Update the frequency of the current character in sMap

            # If the window size is greater than or equal to the size of p
            if i >= len(p) - 1:
                if sMap == pMap:  # If the current window's character frequencies match p's character frequencies
                    res.append(l)  # Append the start index of the current window to the result list
                
                if s[l] in sMap:  # If the character at the left pointer is in sMap
                    sMap[s[l]] -= 1  # Decrement the frequency of that character in sMap
                    if sMap[s[l]] == 0:  # If the frequency becomes zero, remove the character from sMap
                        del sMap[s[l]]
                l += 1  # Move the left pointer to the right
        
        return res  # Return the result list containing starting indices of all anagrams

