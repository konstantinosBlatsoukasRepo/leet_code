class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        return str(int("".join(str(k) for k in digits)) + 1).split(" ")[0]


class Zeroes:
    def moveZeroes(self, nums):
        non_zero_index = 0
        for i, num in enumerate(nums):
            if num != 0:
                nums[non_zero_index] = nums[i]
                non_zero_index += 1



class Solution:
    def reverseString(self, s: List[str]) -> None:
        start = 0
        end = len(s)
        while start < end:
            temp = s[end]
            s[end] = s[start]
            s[start] = temp
            start += 1
            end -= 1