class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
 
        if not strs:  # Check if the list is empty
            return ""

        # Take the first string as the reference to compare with others
        prefix = strs[0]

        # Iterate over all other strings in the list
        for i in range(1, len(strs)):
            # Compare characters with the current prefix
            j = 0
            while j < len(prefix) and j < len(strs[i]) and prefix[j] == strs[i][j]:
                j += 1
            # Update the prefix to the common part
            prefix = prefix[:j]

            # If the prefix becomes empty, return early
            if not prefix:
                return ""

        return prefix

