class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 0:
            return len([num for num in bin(n)[3:] if num == '1'])
        return len([num for num in bin(n)[2:] if num == '1'])
