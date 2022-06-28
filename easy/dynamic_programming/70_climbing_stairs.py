class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """

        def calc_total_ways(i, n, memo):
            if i > n:
                return 0

            if i == n:
                return 1

            if memo[i] > 0:
                return memo[i]

            memo[i] = calc_total_ways(i + 1, n, memo) + calc_total_ways(i + 2, n, memo)
            return memo[i]

        memo = [0 for _ in range(0, n)]

        return calc_total_ways(0, n, memo)
