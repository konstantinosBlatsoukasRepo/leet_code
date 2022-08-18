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


# dynamoc programming
class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1

        solutions = [0 for i in range(n)]
        solutions[0] = 1
        solutions[1] = 2

        for i in range(2, n):
            solutions[i] = solutions[i - 1] + solutions[i - 2]

        return solutions[n -1]