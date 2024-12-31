def knightDialer( n: int) -> int:
        arr = [1] *10 #    def knightDialer(self, n: int) -> int:
       
        MOD = 10**9 +7
        for i in range(2,n+1):
            copy = arr.copy()
            arr[1] =  copy[8]+copy[6]
            arr[2] =  copy[9]+copy[7]
            arr[3] = copy[8]+copy[4]
            arr[4] = copy[3] + copy[9]+ copy[0]
            arr[5]=0
            arr[6]= copy[7] + copy[1]+ copy[0]
            arr[7] = copy[2] + copy[6]
            arr[8] = copy[1]+copy[3]
            arr[9] = copy[2]+copy[4]
            arr[0] = copy[6] + copy[4]

        ans =sum(arr)% MOD
        return ans

print(knightDialer(1))
