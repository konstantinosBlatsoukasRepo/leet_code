# nice trick, identification of a box based on the tuple (r/3, c/3) python: (int(r/3), int(c/3))
# What do they have in common? Every group of three belonging to the same box has the same outcome when we perform integer division by three.
# Therefore, we can use r/3 (/ signifies floor division) to ensure that the rows are grouped as expected and use c/3 to ensure that the columns are grouped correctly.
# Then, (r/3, c/3) can uniquely mark each box, and we can directly use the tuple as the hash key if we want to create a hash set for each box.

class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        def validate_rows(board):
            for row_index in range(len(board)):
                nums = [num for num in board[row_index] if num != '.']
                if len(nums) != len(set(nums)):
                    return False
            return True

        def validate_columns(board):
            for column_index in range(len(board[0])):
                current_col_nums = set()
                for row_index in range(len(board)):
                    prev_length = len(current_col_nums)
                    if board[row_index][column_index] != '.':
                        current_col_nums.add(board[row_index][column_index])
                        if prev_length != len(current_col_nums) - 1:
                            return False
            return True

        def validate_sub_tables(board):
            sub_tables_ranges = [(0, 0), (0, 3), (0, 6)
                                 (3, 0), (3, 3), (3, 6),
                                 (6, 0), (6, 3), (6, 6)]

            for start_row, start_column in sub_tables_ranges:
                nums = set()
                for row in range(start_row, start_row + 3):
                    for column in range(start_column, start_column + 3):
                        prev_length = len(nums)
                        if board[row][column] != '.':
                            nums.add(board[row][column])
                            if prev_length != len(nums) - 1:
                                return False
            return True

        return validate_rows(board) and validate_columns(board) and validate_sub_tables(board)

        # return validate_rows(board)


nums = [1, 2, 3, 3]
print(set(nums))
print(len(set(nums)))


board = [["8", "3", ".", ".", "7", ".", ".", ".", "."], ["6", ".", ".", "1", "9", "5", ".", ".", "."], [".", "9", "8", ".", ".", ".", ".", "6", "."], ["8", ".", ".", ".", "6", ".", ".", ".", "3"], ["4", ".", ".", "8",
                                                                                                                                                                                                      ".", "3", ".", ".", "1"], ["7", ".", ".", ".", "2", ".", ".", ".", "6"], [".", "6", ".", ".", ".", ".", "2", "8", "."], [".", ".", ".", "4", "1", "9", ".", ".", "5"], [".", ".", ".", ".", "8", ".", ".", "7", "9"]]

sol = Solution()
print(sol.isValidSudoku(board))
