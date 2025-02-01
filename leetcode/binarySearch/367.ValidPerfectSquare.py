def isPerfectSquare( num) :
         # for i in range(1,num+1):
        #     if i*i == num:
        #         return True
        #     elif i*i > num:
        #         return False
        l = 0
        r = num
        while l<=r:
            m = (l+r)//2
            if m*m < num:
                l = m+1
            elif m*m > num:
                r = m-1
            else:
                return True
        return False
print(isPerfectSquare(16))