class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res, part = [], []  # Initialize an empty list for results and an empty list for the current partition

        def dfs(i):
            if i >= len(s):  # Base case: if i is beyond the length of s, add the current partition to results
                res.append(part.copy())
                return
            for j in range(i, len(s)):  # Iterate over possible end indices for substrings starting from index i
                if self.isPali(s, i, j):  # Check if the substring s[i:j+1] is a palindrome
                    part.append(s[i : j + 1])  # If it is a palindrome, add it to the current partition
                    dfs(j + 1)  # Recursively call dfs starting from j+1 to find more palindromic partitions
                    part.pop()  # Backtrack: remove the last added substring to explore other possibilities

        dfs(0)  # Start the depth-first search (dfs) from index 0
        return res  # Return the list of all palindromic partitions

    def isPali(self, s, l, r):
        while l < r:  # Iterate from both ends towards the center of the substring
            if s[l] != s[r]:  # If characters at positions l and r are not equal, it's not a palindrome
                return False
            l, r = l + 1, r - 1  # Move towards the center
        return True  # If the loop completes without finding unequal characters, it's a palindrome
