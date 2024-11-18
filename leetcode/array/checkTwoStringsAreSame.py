def checkAlmostEquivalent(word1: str, word2: str) -> bool:
        f1, f2 = [0] * 26, [0] * 26
        
        for ch in word1:
            f1[ord(ch) - ord('a')] += 1
            
        for ch in word2:
            f2[ord(ch) - ord('a')] += 1
        
        for i in range(26):
            if abs(f1[i] - f2[i]) > 3:
                return False
            
        return True

print(checkAlmostEquivalent( "abcdeef","abaaacc"))