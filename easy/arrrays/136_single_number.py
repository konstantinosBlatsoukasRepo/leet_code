# a⊕0=a
# a⊕a=0
#  ba⊕b⊕a=(a⊕a)⊕b=0⊕b=b

import collections

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return collections.Counter(nums).most_common()[-1][0]
