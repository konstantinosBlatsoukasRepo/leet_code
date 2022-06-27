# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """

        if head.next is None:
            return None

        if not head:
            return head

        count = 0
        curr_node = head
        while curr_node:
            count += 1
            curr_node = curr_node.next

        if count == n:
            return head.next

        target_index = count - n

        index = 0
        curr_node = head
        while True:
            if index == target_index - 1:
                curr_node.next = curr_node.next.next
                return head

            index += 1
            curr_node = curr_node.next



