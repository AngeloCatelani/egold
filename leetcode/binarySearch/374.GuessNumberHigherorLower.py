def guessNumber(self, n: int) -> int:
        l=1
        r = n
        
        while l<=r:
            m = (l+r)//2
            guessed = guess(m)
            if guessed == 1:
                l = m+1
            elif guessed == -1:
                r = m-1
            else:
                return m