class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        
        l = 0
        r = len(letters)-1
        while l <= r:
            m = (l+r)//2
            if letters[m]  > target:
                r = m-1
            else:
                l = m+1
        return letters[l % len(letters)]