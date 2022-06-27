import re


class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.strip()

        is_negative = False
        if s[0] == '-':
            is_negative = True

        res = str([a for a in re.split("\D+", "  123 asdsa")
                   if a != ''][0]).lstrip('0')

        if is_negative:
            res = '-' + res

        if int(res) > (2 ** 31) - 1:
            return (2 ** 31) - 1

        if int(res) < -(2 ** 31):
            return -(2 ** 31)

        return int(res)
