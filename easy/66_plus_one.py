class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        return str(int("".join(str(k) for k in digits)) + 1).split(" ")[0]
