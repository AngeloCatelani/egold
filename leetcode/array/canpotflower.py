def canPlaceFlowers( flowerbed, n):
    for i in range(len(flowerbed)):
        if n ==0: return True
        elif ((flowerbed[i-1]==0 or i ==0)and (flowerbed[i]==0)and (i==len(flowerbed)-1 or flowerbed[i+1]==0)):
            flowerbed[i]=1
            n-=1
    return n==0
            