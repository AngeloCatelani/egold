class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        # Inner function to determine if the given string s matches the pattern t
        def is_match(s, t):
            # Initialize two maps for characters in s and t
            # Each map stores the index of the character from s/t encountered in the string
            map_s, map_t = [0] * 128, [0] * 128
            # Enumerate through the pair(s) from s and t
            for index, (char_s, char_t) in enumerate(zip(s, t), 1):
                # If the mappings are not equal, then s does not match the pattern t
                if map_s[ord(char_s)] != map_t[ord(char_t)]:
                    return False
                # Update the mapping for the current character in both s and t to the current index
                map_s[ord(char_s)] = map_t[ord(char_t)] = index
            # If the loops completes without returning False, s matches the pattern t
            return True

        # List comprehension to find and collect words that match the pattern
        # It invokes the is_match function on each word with the given pattern
        return [word for word in words if is_match(word, pattern)]

        # O(N * K), where N is the length of the words list and K is the length of each word (and the pattern). 