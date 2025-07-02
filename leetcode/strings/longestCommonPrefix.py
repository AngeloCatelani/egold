# def longestCommonPrefix(strs):
#     if not strs: return ""
#     if len(strs) == 1: return strs[0]
#     strs.sort()
#     first = strs[0]
#     last = strs[-1]
#     for i, char in enumerate(first):
#         if char != last[i]:
#             print(first[:i])
#             return first[:i]
#     return first

# strs = ["flower","flow","flight"]
# longestCommonPrefix(strs)


def longestCommonPrefix(strs):
  # res=""
  # for i in range(len(strs[0])):
  #   for s in strs:
  #       if i == len(s) or s[i] != strs[0][i]: #without this check for i==len(s) also works
  #           return res
       
  #   res += strs[0][i]
  # return res
        prefix = strs[0]
        for i in range(1,len(strs)):
          current = strs[i]
          res = ""
          for j in range(len(current)):
            if j < len(prefix) and current[j] == prefix[j]:
              res +=prefix[j]
            else:
              break
          prefix = res
        return prefix
strs = ["flower","flow","flight"]
print(longestCommonPrefix(strs))

# time complexity = O(n*m)
# space = O(1)