class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        return str(x)[::-1] == str(x)

sol = Solution()

assert sol.isPalindrome(121) == True
assert sol.isPalindrome(-121) == False
assert sol.isPalindrome(10) == False
