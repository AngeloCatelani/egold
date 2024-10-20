class Solution:
    def firstUniqChar(self, s: str) -> int:
        import collections
        count = collections.Counter(list(s)) 
        for i in range(len(s)):
            if count.get(s[i]) == 1:
                return 1
        return -1

# class Solution:
#     def firstUniqChar(self, s: str) -> int:
#         # myset = set(s)
#         # print(myset,"myset")
#         count = Counter(list(s))
#         # print(count,"count") Counter({'e': 3, 'l': 1, 't': 1, 'c': 1, 'o': 1, 'd': 1}) count
#         for i in range(len(s)):
#             print(count.get(s[i]),"i")
#             if count.get(s[i]) ==1:
#                 return i
            
#         return -1