class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        output =""
        arr = s.split(" ")
        for i in range(len(arr)):
            output += self.reverse(arr[i]) + " "
        return output.rstrip()
    def reverse(self,a):
        out = ""
        for i in range(len(a)-1,-1,-1):
            out += a[i]
        return out


        