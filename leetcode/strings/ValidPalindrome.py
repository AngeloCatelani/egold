class Solution:
    def isPalindrome(self, s: str) -> bool:
        # have two pointers l,r
        # l will increment and right will decement
        # 

        l,r = 0 , len(s)-1
        while l< r:
            while l < r and not self.alphanumeric(s[l]):
                l+=1
            while r > l and not self.alphanumeric(s[r]):
                r-=1
            if s[l].lower() != s[r].lower():
                return False
            else:
                l,r = l+1, r-1
        return True

# Time complexity =O(n)
# space = O(1)


    def alphanumeric(self,c):
        # checking with ASCII values
    #   print(ord("A"),"a")
    #   print(ord(c),"c")
      return ((ord("A") <= ord(c) <=ord("Z")) or    (ord("a") <= ord(c) <=ord("z")) or     (ord("0") <= ord(c) <=ord("9"))    )