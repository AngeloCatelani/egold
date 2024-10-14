# class Solution:
#     def reverseString( s) -> None:
#         """
#         Do not return anything, modify s in-place instead.
#         """
#         # s.reverse()
#         arr = []
#         i = len(s) - 1
#         while i >= 0:
#           arr.append(s[i])
#           i -= 1
#           print(arr,"arr")
#         return arr
#     #    The time and Space complexity of this solution is O(n). It takes O(n) space just because we take a new array for storing elements where n is the size of the array

#     s = ["h","e","l","l","o"]
#     print(reverseString(s))

class Solution:
    def reverseString( s) -> None:
        start = 0
        end = len(s)-1

        while start < end:
            s[start],s[end] = s[end],s[start]
            start +=1 #moving forward
            end-=1 # moving backward
    s = ["h","e","l","l","o"]
    print(reverseString(s))