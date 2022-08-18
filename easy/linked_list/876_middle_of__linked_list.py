# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # count total linked list length
        temp = head
        count = 0
        while temp:
            temp = temp.next
            count += 1

        middle = int(count / 2) + 1

        count = 0
        while head:
            count += 1
            if count == middle:
                return head

            head = head.next


## better approach fast slow pointer!!!!!!!!
class Solution:
    def middleNode(self, head):
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow