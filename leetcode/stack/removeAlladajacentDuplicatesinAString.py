def removeDuplicates( s: str, k: int) -> str:
        stack = [] #char,count [[char,count],[char,count]]
        for c in s:
            if stack and stack[-1][0] == c: # stack[-1][0] is last element's first character
                stack[-1][1] +=1
            else:
                stack.append([c,1]) #[['a', 1], ['b', 1], ['c', 1], ['d', 1]]
            if stack[-1][1] == k:
                stack.pop()
        res = ""
        for char,count in stack:
            res += (char * count) 
        return res
print(removeDuplicates("abcd",2))
print(removeDuplicates("pbbcggttciiippooaais",2))
# time -O(n)
# space - O(n)
