# Two Pointers
# java solution

# public int removeElement(int[] nums, int val) {
#     int i = 0;
#     for (int j = 0; j < nums.length; j++) {
#         if (nums[j] != val) {
#             nums[i] = nums[j];
#             i++;
#         }
#     }
#     return i;
# }

# fast runner and slow runner

class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        slow = 0
        for fast in range(len(nums)):
            if nums[fast] != val:
                nums[slow] = nums[fast]
                slow += 1

        return slow
