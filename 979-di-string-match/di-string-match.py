class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        l = 0
        r = len(s)
        arr =[]

        for char in s:
            if char == "I":
                arr.append(l)
                l +=1
            else:
                arr.append(r)
                r-=1
        arr.append(l)
        return arr
        