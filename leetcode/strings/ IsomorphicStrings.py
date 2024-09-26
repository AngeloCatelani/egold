class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # using hash map as reading and inserting is O(n) going over two strings
        # Space complexity-O(n) because {}

      mapstoT , mapttoS = {},{} # creating two empty hashmaps
      for i in range(len(s)): # going over the length of one of string as both strings are same size
        c1,c2 = s[i], t[i]    # assigning c1,c2 values of s and t at index

        if((c1 in mapstoT and mapstoT[c1] != c2)or (c2 in mapttoS and mapttoS[c2] !=c1)): #checking c1 present in  mapstoT and  mapstoT [c1] value to be c2 if they are not same false
            return False
        else:
            mapstoT[c1] = c2
            mapttoS[c2] = c1
            print (c1 , c2)
            print(mapstoT)
      return True

