# a better solution would be to XOR everything

import collections

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return collections.Counter(nums).most_common()[-1][0]


