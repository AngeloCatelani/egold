class Solution(object):
    def reversePrefix(self, word, ch):
        """
        :type word: str
        :type ch: str
        :rtype: str
        """
        l = 0
        r = 0
        index = 0
        output = ""
        while l < len(word) and r < len(word):
            if word[r] != ch:
                r +=1
            elif word[r] == ch:
                index = r+1
                output += self.reverse(word[l:r+1])
                print(output)
                break

        return output+word[index:]
    def reverse(self,word):
        return "".join(word[::-1])