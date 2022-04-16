## Challenge: remove IN PLACE, no extra memory usage
## Trick: use of an extra index

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        current_index = 0
        current_num = nums[current_index]
        for num in nums:
            if current_num != num:
                nums[current_index + 1] = num
                current_num = num
                current_index += 1

        return current_index + 1