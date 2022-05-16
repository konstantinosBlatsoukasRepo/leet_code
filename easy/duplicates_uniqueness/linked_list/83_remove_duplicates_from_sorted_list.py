# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        return self.deleteDups(head, head)

    def deleteDups(self, root, node):
        if node is None or (node is not None and node.next is None):
            return root

        if node is not None and node.next is not None and node.val == node.next.val:
            node.next = node.next.next
            return self.deleteDups(root, node)

        if node.val != node.next.val:
            return self.deleteDups(root, node.next)
