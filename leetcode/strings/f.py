def areAlmostEquivalent(s, t):
    # Write your code here
    arr = []
    countS = [0]*26
    countT = [0]*26
    for i in s:
        print(i,"i")
        countS[ord(i) - ord("a")]+=1
    for i in t:
        countT[ord(i) - ord("a")] +=1
    for j in range(26):
        if (countS[j] - countT[j]) <= 3:
            arr.append("YES")
        else:
            arr.append("NO")
    return arr
