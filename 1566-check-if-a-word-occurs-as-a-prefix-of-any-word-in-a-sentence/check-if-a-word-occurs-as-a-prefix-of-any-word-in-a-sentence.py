class Solution(object):
    def isPrefixOfWord(self, sentence, searchWord):
        """
        :type sentence: str
        :type searchWord: str
        :rtype: int
        """
        arr = sentence.split(" ")
        for r in range(len(arr)):
            if arr[r].startswith(searchWord):
                return r+1
        return -1