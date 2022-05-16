## search in iterative fashion, bfs using queue (e.g. level by level)

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def searchBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """

        if root is None:
            return None

        queue = [root]

        while queue:

            current_node = queue.pop(0)
            if current_node.val == val:
               return current_node

            if current_node.left is not None:
                queue.append(current_node.left)

            if current_node.right is not None:
                queue.append(current_node.right)

        return None

## recursively

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def searchBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """

        if root:

            if root.val == val:
                return root

            left_res = self.searchBST(root.left, val)
            if left_res is not None and left_res.val == val:
                return left_res

            right_res = self.searchBST(root.right, val)
            if right_res is not None and right_res.val == val:
                return right_res

        return None












