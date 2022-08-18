# first the // operation happens and then the multiplication

# always the  // results in integer value, for example: 5 // 2 == 2

class Solution:
    def longestPalindrome(self, s):
        ans = 0
        for v in collections.Counter(s).values():
            ans += v // 2 * 2
            if ans % 2 == 0 and v % 2 == 1:
                ans += 1
        return ans