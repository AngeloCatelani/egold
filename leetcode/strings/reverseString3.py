class Solution:
    def reverseWords(self, s: str) -> str:
        str = s.split()
        # print(str)
        string=""
        for i in range(len(str)):
          reversed = self.reverse(str[i])
        #   print(reversed,"reversed")
          string += ''.join(reversed)+" "
        return string.strip() # remove empty space from beginning and end


    def reverse(self,c):
        # print(c,"s")
        arr = [*c]
        # print(arr,"arr")
        start = 0
        end = len(c)-1

        while start < end:
            arr[start],arr[end] = arr[end],arr[start]
            start+=1
            end-=1
        return arr
    # print(reverse("LeetCode"))