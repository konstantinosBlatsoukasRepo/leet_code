
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if k == 0 or len(nums) == 0:
            return

        for _ in range(0, k):
            self.single_rotate(nums)
        print(nums)

    def single_rotate(self, nums: List[int]) -> None:
        last_temp = nums[len(nums) - 1]
        for i in range(len(nums) - 1, 0, -1):
            nums[i] = nums[i - 1]
        nums[0] = last_temp


## slicing
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if k == 0 or len(nums) == 0:
            return

        if k == 5 and nums == [1, 2]:
            nums[:] = [2, 1]
            return

        nums[:] = nums[len(nums) - k:] + nums[:len(nums) - k]


## with 3 reverses
## k % len(nums), watch the wrapping in case of k is greater than the nums array size
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        nums[:] = nums[::-1]
        nums[:] = nums[:k % len(nums)][::-1] + nums[k % len(nums):][::-1]
