
from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        max_profit = 0
        for i in range(0, len(prices) - 1):
            diff = prices[i + 1] - prices[i]
            if diff > 0:
                max_profit += diff
        return max_profit


sol = Solution()
assert sol.maxProfit([7, 1, 5, 3, 6, 4]) == 7
assert sol.maxProfit([1, 2, 3, 4, 5]) == 4
assert sol.maxProfit([7, 6, 4, 3, 1]) == 0
