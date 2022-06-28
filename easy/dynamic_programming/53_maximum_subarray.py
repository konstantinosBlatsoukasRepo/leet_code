# kadanes algorithm

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        current_subarray = nums[0]
        max_subarray = nums[0]
        for num in nums[1:]:
          current_subarray = max(num, current_subarray + num)
          max_subarray = max(max_subarray, current_subarray)

        return max_subarray