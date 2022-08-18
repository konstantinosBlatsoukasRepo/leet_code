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

        list_length = self.get_list_length(head)

        if list_length == n:
            return head.next

        return self.remove_nth_node(n, list_length, head)

    def get_list_length(self, head):
        list_length = 0
        curr_node = head
        while curr_node:
            list_length += 1
            curr_node = curr_node.next
        return list_length

    def remove_nth_node(self, n, list_length, head):
        target_index = list_length - n

        index = 0
        curr_node = head
        while True:
            if index == target_index - 1:
                curr_node.next = curr_node.next.next
                return head

            index += 1
            curr_node = curr_node.next


