# Floyds Tortoise and hare algorithm
# using two pointers fast and slow
# space complexity is O(1)

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

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
