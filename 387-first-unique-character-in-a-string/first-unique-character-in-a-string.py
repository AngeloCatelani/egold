class Solution:
    def firstUniqChar(self, s: str) -> int:
        count = Counter((s))
        # print(count)Counter({'e': 3, 'l': 1, 't': 1, 'c': 1, 'o': 1, 'd': 1})
        for i in range(len(s)):
            if count.get(s[i]) ==1:
                return i
            
        return -1

