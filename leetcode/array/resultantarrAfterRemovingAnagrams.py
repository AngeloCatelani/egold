def removeAnagrams(words):
        stack = []
        for w in words:
            if len(stack) == 0 or sorted(w) != sorted(stack[-1]):
                stack.append(w)
        return stack
print(removeAnagrams(["abba","baba","bbaa","cd","cd"]))