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
    


     left, right = 0, len(s) - 1 
 
    while left < right:
        while left < right and not s[left].isalnum():
            left +=1
        while right > left and not s[right].isalnum():
            right -= 1
        if s[left].lower() != s[right].lower():
            return False 
        left, right = left + 1, right - 1
    return True
The time complexity for this solution is O(n) because you are still looping through the entire string. The space complexity is O(1) because you are not making a new string.