class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
         # Split the string into words
        words = s.split()
        # Reverse the list of words
        words.reverse()
        # Join the reversed words back into a string
        return ' '.join(words)
