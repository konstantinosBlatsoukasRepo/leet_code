class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return int((len(nums) * (len(nums) + 1)) / 2) - sum(nums)
