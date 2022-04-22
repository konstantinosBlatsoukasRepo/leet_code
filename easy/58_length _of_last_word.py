import re

class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        splited = re.split("\s+", s.lstrip().rstrip())
        if len(splited) == 0:
            return 0

        return len(splited[-1])
