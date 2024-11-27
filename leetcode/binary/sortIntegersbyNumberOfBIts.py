def sortByBits(arr) :
        stack = []

        for n in arr:
            count = bin(n)[2:].count("1")
            stack.append([count, n])
        
        stack.sort()
        arr = [num for c, num in stack]
        return arr
print(sortByBits([0,1,2,3,4,5,6,7,8]))