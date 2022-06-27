# you could solve that using sort and two indices
# only one map is enough

from collections import Counter


class Solution():
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """

        def get_intersection(nums1, nums2):
            num1Count = Counter(nums1)
            num2Count = Counter(nums2)
            intersection = []
            for key in num2Count:

                if key in num1Count:
                    num1_val = num1Count[key]
                    nmum2_val = num2Count[key]
                    if num1_val >= nmum2_val:
                        intersection.extend(
                            [key for i in range(0, nmum2_val)])
                    else:
                        intersection.extend(
                            [key for i in range(0, num1_val)])

            return intersection

        if len(nums1) >= len(nums2):
            return get_intersection(nums1, nums2)

        return get_intersection(nums2, nums1)


nums1 = [4, 9, 5]
nums2 = [9, 4, 9, 8, 4]
sol = Solution()

print(sol.intersect(nums1, nums2))
