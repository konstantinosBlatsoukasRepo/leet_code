## Challenge: to find a solution less than O^2
## Trick: use of a hash map that keeps the seen numbers
## along with the indexes


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        seenNums = {}
        for currentIndx, value in enumerate(nums):
          targetNum = target - value
          if targetNum in seenNums:
            return [seenNums[targetNum], currentIndx]
          seenNums[value] = currentIndx

sol = Solution()

assert sol.twoSum([2,7,11,15], 9) == [0, 1]
assert sol.twoSum([3,2,4], 6) == [1, 2]
assert sol.twoSum([3,3], 6) == [0, 1]