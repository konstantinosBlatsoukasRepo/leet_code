# from collections import Counter


# class Solution(object):
#     def isAnagram(self, s, t):
#         """
#         :type s: str
#         :type t: str
#         :rtype: bool
#         """
#         if len(s) != len(t):
#             return False

#         counter_s = Counter(s)
#         counter_t = Counter(t)
#         for i in range(len(s)):
#             if counter_s[s[i]] != counter_t[s[i]]:
#                 return False

#         return True



from collections import Counter


class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        return sorted(s) == sorted(t)
