class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
         # Tuple of Roman numerals in descending order
        roman_symbols = ('M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I')
        # Tuple of the respective values of the Roman numerals
        roman_values = (1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1)
      
        # Will hold the resulting Roman numeral string
        roman_string = []
      
        # Pair Roman symbols with their values
        for symbol, value in zip(roman_symbols, roman_values):
            # As long as the number is greater than or equal to the value
            while num >= value:
                # Subtract the value from the number
                num -= value
                # Append the corresponding Roman symbol to the list
                roman_string.append(symbol)
      
        # Join the list of symbols to get the final Roman numeral string
        return ''.join(roman_string)