# better solution in leetcode no usage of ordered array and no need of level marking

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""


class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """

        if root is None:
            return root

        def storeNodesOrderedBylevel(root):
            nodes = []

            root.level = 1
            queue = [root]
            while queue:
                current_node = queue.pop(0)
                print(current_node)
                if current_node.left is not None:
                    current_node.left.level = current_node.level + 1
                    queue.append(current_node.left)

                if current_node.right is not None:
                    current_node.right.level = current_node.level + 1
                    queue.append(current_node.right)

                nodes.append(current_node)

            return nodes

        orderedNodes = storeNodesOrderedBylevel(root)

        for i in range(len(orderedNodes) - 1):
            current_node = orderedNodes[i]
            next_node = orderedNodes[i + 1]

            if current_node.level != next_node.level:
                current_node.next = None
            else:
                current_node.next = next_node

        return root


# import collections

# class Solution:
#     def connect(self, root: 'Node') -> 'Node':

#         if not root:
#             return root

#         # Initialize a queue data structure which contains
#         # just the root of the tree
#         Q = collections.deque([root])

#         # Outer while loop which iterates over
#         # each level
#         while Q:

#             # Note the size of the queue
#             size = len(Q)

#             # Iterate over all the nodes on the current level
#             for i in range(size):

#                 # Pop a node from the front of the queue
#                 node = Q.popleft()

#                 # This check is important. We don't want to
#                 # establish any wrong connections. The queue will
#                 # contain nodes from 2 levels at most at any
#                 # point in time. This check ensures we only
#                 # don't establish next pointers beyond the end
#                 # of a level
#                 if i < size - 1:
#                     node.next = Q[0]

#                 # Add the children, if any, to the back of
#                 # the queue
#                 if node.left:
#                     Q.append(node.left)
#                 if node.right:
#                     Q.append(node.right)

#         # Since the tree has now been modified, return the root node
#         return root