# Floyds Tortoise and hare algorithm
# using two pointers fast and slow
# space complexity is O(1)

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

from collections import deque


class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        return self.hasCycleInner(head, [])

    def hasCycleInner(self, head, seen):
        if head is None:
            return False

        if head.next in seen:
            return True

        seen.append(head)
        return self.hasCycleInner(head.next, seen)


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head) -> bool:
        if not head:
            return False

        fast = head
        slow = head
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return True

        return False


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root):
        if root is None:
            return 0

        left = self.maxDepth(self, root.left) + 1
        right = self.maxDepth(self, root.right) + 1
        return max(left, right)


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        queue = deque([root])
        level = 0
        while queue:

            total_level_nodes = len(queue)
            # remove current level nodes and add next level nodes
            for _ in range(total_level_nodes):
                curr_node = queue.popleft()
                if curr_node.right:
                    queue.append(curr_node.right)
                if curr_node.left:
                    queue.append(curr_node.left)

            level += 1

        return level


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        if not root:
            return True

        queue = deque([root])

        while queue:
            new_nodes = deque([])
            total_level_nodes = math.ceil(len(queue) / 2)

            for _ in range(total_level_nodes):

                if len(queue) == 1:
                    node = queue.pop()
                    new_nodes.append(node.left)
                    new_nodes.append(node.right)
                elif queue:

                    left_node = queue.popleft()
                    right_node = queue.pop()

                    if right_node is not None and left_node is None:
                        return False

                    if left_node is not None and right_node is None:
                        return False

                    if left_node and right_node:

                        if left_node.val != right_node.val:
                            return False
                        else:
                            new_nodes.appendleft(left_node.right)
                            new_nodes.appendleft(left_node.left)
                            new_nodes.append(right_node.left)
                            new_nodes.append(right_node.right)

            queue = new_nodes

        return True


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        result = []
        if root is None:
            return result

        queue = deque([root])
        while queue:

            level_nodes = []
            for _ in range(len(queue)):

                extracted_node = queue.popleft()
                level_nodes.append(extracted_node.val)

                if extracted_node.left:
                    queue.append(extracted_node.left)

                if extracted_node.right:
                    queue.append(extracted_node.right)

            result.append(level_nodes)

        return result
