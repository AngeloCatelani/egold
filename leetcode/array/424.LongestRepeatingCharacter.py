def characterReplacement( s: str, k: int) -> int:
        res = 0
        l =0
        charset = set()

        for r in range(len(s)):
            while s[r] in charset:
                charset.remove(s[l])
                l+=1
            # s[r] = s[l]
            charset.add(s[l])
            res = max(res,r-l+1)
        return res
print(characterReplacement( "ABAB", 2))