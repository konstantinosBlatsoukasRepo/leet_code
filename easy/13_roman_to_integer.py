# Challenge: to find a solution less than O^2
# keys:
# 1. start from the end chars and move forward
# 2. how to take last n chars my_list[-2:]

romanToInt = {
    "I": 1,
    "IV": 4,
    "V": 5,
    "IX": 9,
    "X": 10,
    "XL": 40,
    "L": 50,
    "XC": 90,
    "C": 100,
    "CD": 400,
    "D": 500,
    "CM": 900,
    "M": 1000
}


class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        return self.convert(s, 0)

    def convert(self, s, result):
        if len(s) == 0:
            return result

        if len(s) > 1 and s[-2:] in romanToInt:
            return self.convert(s[0:len(s)-2], result + romanToInt[s[-2:]])
        return self.convert(s[0:len(s)-1], result + romanToInt[s[-1:]])


sol = Solution()

assert sol.romanToInt("III") == 3
assert sol.romanToInt("LVIII") == 58
assert sol.romanToInt("MCMXCIV") == 1994
