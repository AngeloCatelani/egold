class Solution(object):
    def strStr(self,haystack, needle):
        if not needle:
            return 0
        
        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i:i+len(needle)] == needle:
                return i
        
        return -1

# This implementation works as follows:

# First, we check if the needle is an empty string. If it is, we return 0 as per the problem's requirements.

# We then iterate through the haystack string, but only up to the point where there are enough characters left to potentially match the needle.

# For each position, we check if the substring of haystack starting at that position and of length equal to the needle matches the needle.

# If we find a match, we immediately return the starting index.

# If we complete the loop without finding a match, we return -1.
#         Time Complexity: O(n*m), where n is the length of haystack and m is the length of needle.
# Space Complexity: O(1), as we're not using any extra space that grows with input size.