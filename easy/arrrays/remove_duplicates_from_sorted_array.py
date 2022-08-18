# checking previous and next with the help of an extra index
# This is also called two pointers

class Solution(object):
    def removeDuplicates(self, nums):

        current_index = 0
        for i in range(0, len(nums) - 1):
            if nums[i + 1] != nums[i]:
                current_index += 1
                nums[current_index] = nums[i + 1]

        return current_index + 1
