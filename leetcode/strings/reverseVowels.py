class Solution:
    def reverseVowels( s: str) -> str:
        # vowels="aeiou"
        # check each letter is vowels if vowels swap position of another vowel
        vowels = "aeiou"
        # arr=[*s] to convert string to array
        # print([*s])
        # print(arr,"arr")
   
        # vowels="aeiou"
        # check each letter is vowels if vowels swap position of another vowel
        arr = list(s)
        start = 0
        end = len(s) -1

        while start < end:
            if arr[start] not in "aeiouAEIOU":
                start+=1
            elif arr[end] not in "aeiouAEIOU":
                end-=1
            else:
                arr[start],arr[end] = arr[end],arr[start]
                start+=1
                end-=1
        return "".join(arr)
    s="hello"
    print(reverseVowels(s))