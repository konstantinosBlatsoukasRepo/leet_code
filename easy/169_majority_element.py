# Boyer-Moore, linera time, no extra space
# class Solution:
#     def majorityElement(self, nums):
#         count = 0
#         candidate = None

#         for num in nums:
#             if count == 0:
#                 candidate = num
#             count += (1 if num == candidate else -1)

#         return candidate
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        nums.sort()

        best_freq = 1
        current_freq = 1
        maj_ele = nums[0]
        previous = nums[0]

        for i in range(1, len(nums)):
            if previous == nums[i]:
                current_freq += 1
                if current_freq > best_freq:
                    best_freq = current_freq
                    maj_ele = nums[i]
            else:
                current_freq = 1

            previous = nums[i]

        return maj_ele
