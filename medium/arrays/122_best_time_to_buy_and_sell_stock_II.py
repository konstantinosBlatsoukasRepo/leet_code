# one approach is using local min, max (valley, peak)
# other approach is using the positive diffs

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        total = 0
        valley = 10000000000000000
        peak = valley

        for price in prices:
            if price < peak:
                total = total + (peak - valley)
                valley = price
                peak = valley
            else:
                peak = valley

        total = total + (peak - valley)

        return total
