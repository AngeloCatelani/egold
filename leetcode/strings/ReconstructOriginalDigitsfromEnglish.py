
def originalDigits( s: str) -> str:
        import collections
        # zero - z
        # one o -0-2-4
        # two - w
        # three - h -8
        # four - u
        # five - f -4
        # six - x
        # seven -v -5
        # eight - g
        # nine - i-8 -6-5

        count = collections.Counter(s)
        ans = {}
        ans[0] = count["z"]
        ans[2] = count["w"]
        ans[4] = count["u"]
        ans[6] = count["x"]
        ans[8] = count["g"]

        ans[3] = count["h"] - ans[8]
        ans[5] = count["f"] -ans[4]
        ans[7] = count["v"] - ans[5]
        ans[9] = count["i"] - ans[8]-ans[6]-ans[5]
        ans[1] = count["o"] - ans[0]-ans[2]-ans[4]

        output=""
        for i in range(10):
            output +=str(i) * ans[i]
        return output
print(originalDigits("owoztneoer"))
