class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
     # Split string by spaces, strip() handles leading/trailing spaces
        arr = s.split()

        # Initialize an empty list for reversed words
        reversed_words = []

        # Iterate through the array in reverse order and append words to the list
        for i in range(len(arr) - 1, -1, -1):
            reversed_words.append(arr[i])

        # Join the list into a string with single spaces between words
        return " ".join(reversed_words)