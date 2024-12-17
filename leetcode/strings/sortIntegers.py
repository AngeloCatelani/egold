
def getKth( lo: int, hi: int, k: int) -> int:
        def getPower(n):
            result = 0
            while n!=1:
                if n%2==0:
                    n = n//2
                else:
                    n = n * 3 + 1
                result += 1
            return result
        d = []
        for i in range(lo,hi+1):
            d.append([i,getPower(i)])
        d = sorted(d, key=lambda x: x[1]) # In this case, this function takes the single argument x and returns x[1] (i.e. the item at index 1 in x). sorts out on 1 iondex element in d arr
        return d[k-1][0]
print(getKth(12,15,2))
