from collections import Counter


class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        return sorted(s) == sorted(t)



class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        tuples = []
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if i !=- j:
                    tuples.append((i, j))

        numsWithIndex = {}
        for k, num in enumerate(nums):
            numsWithIndex[num] = k


        triples = set()
        for i, j in tuples:
            wantedNum = nums[i] + nums[j]
            if -wantedNum in numsWithIndex:
                print("success")

            if -wantedNum in numsWithIndex and numsWithIndex[wantedNum] != i and numsWithIndex[wantedNum] != j and i != j:
                current_triple = [nums[i], nums[j], nums[numsWithIndex[wantedNum]]]
                current_triple.sort()
                triples.add((current_triple[0], current_triple[1], current_triple[2]))

        return list(triples)