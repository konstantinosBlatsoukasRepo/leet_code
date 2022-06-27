import re


class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """

        chars = ''.join(re.split('\W+|_', s.lower()))
        start = 0
        end = len(chars) - 1

        while (end > start):
            if chars[start] != chars[end]:
                return False

            start += 1
            end -= 1

        return True
