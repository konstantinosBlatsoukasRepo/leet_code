class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        nums.sort() # O(n logn)
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                return True
        return False


class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        return len(nums) != len(set(nums))

