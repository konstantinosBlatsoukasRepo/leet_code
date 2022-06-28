# there is better way using three pointers

class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """

        first_zero_val_index = -1
        for i, val in enumerate(nums1):
            if val == 0 and i >= m:
                first_zero_val_index = i
                break

        for num2_val in nums2:
            nums1[first_zero_val_index] = num2_val
            first_zero_val_index += 1

        nums1.sort()