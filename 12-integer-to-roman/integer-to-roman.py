class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        roman_symbols = ('M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I')
        # Tuple of the respective values of the Roman numerals
        roman_values = (1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1)
        res = []
        for symbols,values in zip(roman_symbols,roman_values):
            while num >= values:
                num -= values
                res.append(symbols)
        return "".join(res)