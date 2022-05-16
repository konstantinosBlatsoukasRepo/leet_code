# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        lengthA = self.get_length(headA, 0)
        lengthB = self.get_length(headB, 0)

        if lengthA > lengthB:
            diff = lengthA - lengthB
            for _ in range(0, diff):
                headA = headA.next
        else:
            diff = lengthB - lengthA
            for _ in range(0, diff):
                headB = headB.next

        while headB and headA:
            if headB == headA:
                return headA
            headB = headB.next
            headA = headA.next

        return None

    def get_length(self, head, acc):
        if head is None:
            return acc
        return self.get_length(head.next, acc + 1)
