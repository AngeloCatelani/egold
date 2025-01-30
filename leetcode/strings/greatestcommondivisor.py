def gcdOfStrings(str1: str, str2: str) -> str:
        if str1 != str2:
            return ""
        for i in range(len(str2)):
            print(i,"i")
            if str1[i] == str2[i]:
                continue
        print(str1[i,len(str1)])
        return str1[i:]

print(gcdOfStrings("ABCABC","ABC"))