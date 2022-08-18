class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0

        numbers = [False, False] + [True] * (n -2)

        for p in range(2, int(sqrt(n)) + 1):
            if numbers[p]:
                for mult in range(p * p, n, p):
                    numbers[mult] = False

        return sum(numbers)
