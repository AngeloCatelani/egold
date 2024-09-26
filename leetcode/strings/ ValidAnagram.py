class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
      if len(s) != len(t): # if not same length return False
        return False
      countS , countT = {} , {} # assigning empty hashmap
      for i in range(len(t)): # first assign each letter the countof letter in string
        countS[s[i]] = 1 + countS.get(s[i],0) #{a:3} if there is no value will take default value 0
        countT[t[i]] = 1 + countT.get(t[i],0)

      for c in countS: #compare strings letter value(count) to t's count
        if countS[c] != countT.get(c, 0): # checking count of a matches hashmap t with same value
            return False
      return True
    
    # #  second solution
    #    return Counter(s) == Counter(t)   #Counter is a subclass of dict that's specially designed for counting hashable objects 
    # #  third solution
    #   return sorted(s) == sorted(t)
