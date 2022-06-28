# brute force
# time complexity O(n^2)
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        max_diff = 0
        for i in range(0, len(prices)):
            for j in range(i + 1, len(prices)):
                if prices[j] - prices[i] > max_diff:
                    max_diff = prices[j] - prices[i]

        return max_diff


# one pass
# time complexity O(n)
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        largest_diff = 0
        min_so_far = 10000000000000000

        for price in prices:
            if price < min_so_far:
                min_so_far = price
            else:
                largest_diff = max(largest_diff, price - min_so_far)

        return largest_diff