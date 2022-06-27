from collections import deque
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """

        if root is None:
            return []

        queue = deque()
        root.level = 0
        queue.append(root)

        levels = [[root.val]]
        while queue:
            node = queue.popleft()
            for child in node.children:
                child.level = node.level + 1
                queue.append(child)
                if child.level < len(levels):
                    levels[child.level].append(child.val)
                else:
                    levels.append([child.val])

        return levels


# ! better solution!!!
# class Solution:
#     def levelOrder(self, root: Optional['Node']) -> List[List[int]]:
#         if root is None:
#             return []
#         result = []
#         queue = collections.deque([root])
#         while queue:
#             level = []
#             for _ in range(len(queue)):
#                 node = queue.popleft()
#                 level.append(node.val)
#                 queue.extend(node.children)
#             result.append(level)
#         return result
