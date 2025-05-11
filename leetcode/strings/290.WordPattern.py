def wordPattern( pattern: str, s: str) -> bool:
        # have two hashmap one for pattern and another for s
        # if both not same length return False
        
        word = s.split()
        if len(pattern) != len(word):
            return False
        charToWordHash = {}
        wordToCharHash = {}
       
        for c,w in zip(pattern,word):
            if c in charToWordHash and charToWordHash[c] != w:
                return False
            if w in wordToCharHash and wordToCharHash[w] != c:
                return False

            charToWordHash[c] = w
            wordToCharHash[w] = c

        return True

    # time(n+m)
print(wordPattern("abba","dog cat cat dog"))