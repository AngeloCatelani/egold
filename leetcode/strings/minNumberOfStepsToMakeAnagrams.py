def minSteps( s: str, t: str) -> int:
        steps = 0
        count = [0]*26
        

        for i in s:
            # print(i)
            count[ord(i) - ord("a")] +=1
        for i in t:
            count[ord(i) - ord("a")] -=1
            # print(countT)
        
        for c in range(26):
            if count[c]>0:
                steps +=count[c]
        return steps
print(minSteps(s = "bab", t = "aba"))
print(minSteps(s = "leetcode", t = "practice"))