# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        return self.travserse(root, [])

    def travserse(self, root, acc):
        if root is None:
            return acc

        if root.val is not None:
            acc.append(root.val)

        if root.left is not None:
            self.travserse(root.left, acc)

        if root.right is not None:
            self.travserse(root.right, acc)

        return acc


# Iterative solution

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []

        if root is None:
            return result

        queue = [root]

        while queue:
            node = queue.pop()  # remove last element from the top of the queue
            result.append(node.val)

            if node.right is not None:
                queue.append(node.right)

            if node.left is not None:
                queue.append(node.left)

        return result
