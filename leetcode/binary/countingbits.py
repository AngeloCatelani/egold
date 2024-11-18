class Solution:
    def countBits(self, n: int) -> List[int]:
        # length of output arr  is n+1
        # i should go still n
        # as per number of 1 in it append the total number of 1's for each i in output arr
        ans=[]
        i=0
        while i <= n:
          ans.append(self.counting1(i))
          i=i+1
        return ans
        

    def counting1(self,n):
        res=0
        while n!=0:
            res +=n%2
            n = n >>1
        return res