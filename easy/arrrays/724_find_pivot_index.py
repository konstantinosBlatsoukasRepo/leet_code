class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total_sum = sum(nums)

        current_sum = 0
        for i in range(len(nums)):
            if total_sum - (current_sum + nums[i]) == current_sum:
                return i
            current_sum += nums[i]
        return -1
