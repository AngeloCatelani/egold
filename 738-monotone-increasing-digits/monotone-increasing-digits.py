class Solution:
    def monotoneIncreasingDigits(self, n: int) -> int:
        # Convert the number to a list of characters for easy manipulation
        digits = list(str(n))

        # Find the first digit that breaks the monotony
        index = 1
        while index < len(digits) and digits[index - 1] <= digits[index]:
            index += 1

        # If a non-monotone digit was found, modify the number
        if index < len(digits):
            # Decrease the previous digit by 1 until the number becomes monotone
            while index > 0 and digits[index - 1] > digits[index]:
                digits[index - 1] = str(int(digits[index - 1]) - 1)
                index -= 1

            # Setting the rest of the digits to '9' to guarantee the largest monotone number
            index += 1
            while index < len(digits):
                digits[index] = '9'
                index += 1

        # Convert the list of characters back to an integer and return
        return int(''.join(digits))