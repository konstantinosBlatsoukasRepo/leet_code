from collections import deque


class Solution(object):
    def shortestPathBinaryMatrix(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        max_row = len(grid) - 1
        max_column = len(grid[0]) - 1

        if grid[0][0] != 0 or grid[max_row][max_column] != 0:
            return -1

        def get_adjacents(row, column, grid):
            candidates = [(row + 1, column), (row + 1, column + 1), (row, column + 1),
                          (row - 1, column + 1), (row - 1,
                                                  column), (row - 1, column - 1),
                          (row, column - 1), (row + 1, column - 1)]

            adjacents = []
            for cand_row, cand_column in candidates:
                if cand_row >= 0 and cand_row <= max_row and cand_column >= 0 and cand_column <= max_column and grid[cand_row][cand_column] == 0:
                    adjacents.append((cand_row, cand_column))
            return adjacents

        queue = deque()
        queue.append((0, 0))

        grid[0][0] = 1

        while queue:
            last_row, last_column = queue.popleft()

            distance = grid[last_row][last_column]

            if last_row == max_row and last_column == max_column:
                return distance

            adjacents = get_adjacents(last_row, last_column, grid)
            for adj_row, adj_column in adjacents:
                grid[adj_row][adj_column] = distance + 1
                queue.append((adj_row, adj_column))

        return -1
