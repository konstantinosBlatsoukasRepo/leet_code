class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        if ((len(nums) == 1 and nums[0] == target) or (len(nums) == 1 and nums[0] != target)) and target < nums[0]:
          return 0
        elif ((len(nums) == 1 and nums[0] == target) or (len(nums) == 1 and nums[0] != target)) and target > nums[0]:
          return 1

        return self.search(0, len(nums) - 1, nums, target)


    def search(self, start, end, nums, target):
      if nums[end] == target:
        return end

      notFound = end - start  == 1 and nums[start] != target and nums[end] != target

      if notFound and nums[end] < target:
        return end + 1
      elif notFound and nums[end] > target and nums[start] < target:
        return start + 1
      elif notFound and nums[end] > target and nums[start] > target:
        return start

      mid = int((start + end) / 2)
      if nums[mid] == target:
        return mid
      elif nums[mid] > target:
        return self.search(start, mid, nums, target)
      elif nums[mid] < target:
        return self.search(mid, end, nums, target)


nums = [1,3,5,6]
target = 0
sol = Solution()

assert sol.searchInsert(nums, target) == 0



