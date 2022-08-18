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


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:

        # build a double linked list
        # save a pointer to last node
        curr = head
        prev = None
        last_node = None
        while curr:
            if curr.next is None:
                # save a pointer to last node
                last_node = curr

            curr.previous = prev
            prev = curr
            curr = curr.next

        # left pointer is initialized at the head of the list
        # and the right pointer at the end of the list
        left_pointer = head
        right_pointer = last_node

        # move the right pointer from right to the left
        # move the left pointer from left to the right
        # if it is a palindrome the values of the two pointers
        # must be equal at each iteration
        while left_pointer != right_pointer:
            if left_pointer.val != right_pointer.val:
                return False

            left_pointer = left_pointer.next
            right_pointer = right_pointer.previous

        return True



class Solution:
    def hasCycle(self, head) -> bool:
        if not head:
            return -1

        valIndexes =  {}

        curr = head
        currIndex = 0
        while curr:
            if curr.val not in valIndexes:
                valIndexes[curr.val] = currIndex
                currIndex += 1
            else:
                return valIndexes[curr.val]

        return -1

