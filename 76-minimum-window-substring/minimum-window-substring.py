class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""

        countS = {}
        countT = {}
        res = [0, 0]  # Initialize with default values
        resLength = float("infinity")
        l = 0

        for char in t:
            countT[char] = 1 + countT.get(char, 0)

        have = 0
        need = len(countT)

        for r in range(len(s)):
            countS[s[r]] = 1 + countS.get(s[r], 0)

            if s[r] in countT and countS[s[r]] == countT[s[r]]:
                have += 1

            while have == need:
                if r - l + 1 < resLength:
                    res = [l, r]
                    resLength = r - l + 1

                countS[s[l]] -= 1
                if s[l] in countT and countS[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1

        l, r = res
        return s[l:r+1] if resLength != float("infinity") else ""
