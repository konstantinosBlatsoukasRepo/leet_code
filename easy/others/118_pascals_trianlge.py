# 1. there is optimal substructure
# 2. there are overlapping subproblems

class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        result = []

        for current_row in range(0, numRows):

            if current_row == 0:
                result.append([1])
            elif current_row == 1:
                result.append([1, 1])
            else:
                new_row = [1] + [0 for _ in range(current_row - 1)] + [1]

                prev_row_col_index = 0
                for j in range(1, len(new_row) - 1):
                    new_row[j] = result[current_row - 1][prev_row_col_index] + \
                        result[current_row - 1][prev_row_col_index + 1]
                    prev_row_col_index += 1

                result.append(new_row)

        return result
