# couldn't solve it


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        if list1 is None:
          return list2
        elif list2 is None:
          return list1
        elif list1.val > list2.val:
          list2.next = self.mergeTwoLists(list1, list2.next)
          return list2
        else:
          list1.next = self.mergeTwoLists(list1.next, list2)
          return list1
