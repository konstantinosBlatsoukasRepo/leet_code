# couldn't manage to solve it
# dynamic programming, memoization, and recursion

class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        def rob(i, nums, mem):
            if i >= len(nums):
                return 0

            if i in mem:
                return mem[i]

            ans = max(rob(i + 1, nums, mem), rob(i + 2, nums, mem) + nums[i])

            mem[i] = ans

            return ans

        mem = {}
        return rob(0, nums, mem)


