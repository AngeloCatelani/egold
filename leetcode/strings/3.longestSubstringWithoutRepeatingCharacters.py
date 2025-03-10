def lengthOfLongestSubstring(self, s: str) -> int:
        # have maxLength =1
        # 
#         if s == "": return 0
#         maxLength = 1
#         for i in range(len(s)):
#             substring = s[i]
#             for j in range(i+1,len(s)):
#                 if s[j] not in substring:
#                     substring +=s[j]
#                     maxLength = max(maxLength,len(substring))
#                 else:
#                     break
#         return maxLength
                
# # time - O(n^2)
            charSet = set()
            l = 0
            res = 0
            for r in range(len(s)):
                while s[r] in charSet:
                    charSet.remove(s[l])
                    l+=1
                charSet.add(s[r])
                res = max(res,r-l+1)
            return res