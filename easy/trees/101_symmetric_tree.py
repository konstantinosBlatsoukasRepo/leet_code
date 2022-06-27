# You have to work with two heads!

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.isMirror(root, root)

    def isMirror(self, left, right):
        if left is None and right is None:
            return True
        elif left is None or right is None:
            return False
        else:
            return left.val == right.val and self.isMirror(left.right, right.left) and self.isMirror(left.left, right.right)

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        queue = [root, root]

        while queue:
            left_tree = queue.pop()
            right_tree = queue.pop()

            if left_tree is None and right_tree is None:
                continue

            if left_tree is None or right_tree is None:
                return False

            if left_tree.val != right_tree.val:
                return False

            queue.append(left_tree.right)
            queue.append(right_tree.left)
            queue.append(left_tree.left)
            queue.append(right_tree.right)

        return True


