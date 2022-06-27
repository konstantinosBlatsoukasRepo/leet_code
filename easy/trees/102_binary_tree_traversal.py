# I was implementing wrong the bfs!!

from collections import deque
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """

        if not root:
            return []

        queue = deque([(0, root)])

        tree_with_levels = [(0, root)]

        while queue:
            level, node = queue.popleft()

            if node.left:
                queue.append((level + 1, node.left))
                tree_with_levels.append((level + 1, node.left))

            if node.right:
                queue.append((level + 1, node.right))
                tree_with_levels.append((level + 1, node.right))

        current_level, current_val = tree_with_levels[0]
        current_result_index = 0
        result = [[current_val.val]]

        if len(tree_with_levels) == 1:
            return result

        for i in range(1, len(tree_with_levels)):
            next_level, next_node = tree_with_levels[i]

            if next_level != current_level:
                result.append([next_node.val])
                current_result_index += 1
                current_level = next_level
            else:
                result[current_result_index].append(next_node.val)

        return result
