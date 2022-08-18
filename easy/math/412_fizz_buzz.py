class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        result = []
        for i in range(1, n + 1):
            current_sol = ""
            if i % 3 == 0 and i % 5 == 0:
                current_sol += "FizzBuzz"
            elif i % 3 == 0:
                current_sol += "Fizz"
            elif i % 5 == 0:
                current_sol += "Buzz"
            else:
                current_sol += str(i)
            result.append(current_sol)
        return result
