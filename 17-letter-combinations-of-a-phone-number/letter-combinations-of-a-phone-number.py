class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # Initialize an empty list to store the result
        res = []

        # Mapping of digits to corresponding characters as on a phone keypad
        digitToChar = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        # Define the backtrack function that will recursively generate combinations
        def backtrack(i, curStr):
            # If the current string's length is equal to the length of digits,
            # it means we have formed a valid combination
            if len(curStr) == len(digits):
                # Add the current string to the result list
                res.append(curStr)
                return
            # Iterate through each character corresponding to the current digit
            for c in digitToChar[digits[i]]:
                # Recur with the next digit index and the current string appended with the current character
                backtrack(i + 1, curStr + c)

        # Start the backtracking process if digits is not empty
        if digits:
            backtrack(0, "")

        # Return the result list containing all possible letter combinations
        return res