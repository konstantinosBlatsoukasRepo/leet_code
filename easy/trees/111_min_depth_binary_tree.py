# LEVEL ORDER TRAVERSAL


# recursive solution
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution(object):
#     def minDepth(self, root):
#         """
#         :type root: TreeNode
#         :rtype: int
#         """

#         if root is None:
#             return 0

#         if root.right is None and root.left is not None:
#             return 1 + self.minDepth(root.left)

#         if root.left is None and root.right is not None:
#             return 1 + self.minDepth(root.right)

#         return 1 + min(self.minDepth(root.right), self.minDepth(root.left))


# iterative solution, using bfs
# increase the depth at each Node!!
class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        queue = [{'node': root, 'depth': 1}]

        while queue:
            currentNode = queue.pop(0)

            if currentNode['node'].left is None and currentNode['node'].right is None:
                return currentNode['depth']

            if currentNode['node'].right is not None:
                queue.append({'node': currentNode['node'].right,
                              'depth': currentNode['depth'] + 1})

            if currentNode['node'].left is not None:
                queue.append({'node': currentNode['node'].left,
                              'depth': currentNode['depth'] + 1})

        return -1
