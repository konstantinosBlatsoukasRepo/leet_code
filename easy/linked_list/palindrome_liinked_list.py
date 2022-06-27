# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head:
            return True

        a = []
        node = head
        while node:
            a.append(node.val)
            node = node.next

        while a:
            val = a.pop()
            if head.val != val:
                return False
            head = head.next

        return True

