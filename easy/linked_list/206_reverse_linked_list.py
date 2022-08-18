# this can be solved using two pointers technique, no need for extra memory allocation

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head):

        list_nodes = []
        current_node = head
        while current_node:
            list_nodes.append(current_node)
            current_node = current_node.next

        for curr_node_index in range(len(list_nodes) - 1, -1 , -1):
            if curr_node_index == 0:
                list_nodes[curr_node_index].next = None
                return list_nodes[len(list_nodes) - 1]

            list_nodes[curr_node_index].next = list_nodes[curr_node_index - 1]


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1, list2):

        cur = dummy = ListNode()

        while list1 and list2:
            if list1.val < list2.val:
                cur.next = list1
                list1, cur = list1.next, list1
            else:
                cur.next = list2
                list2, cur = list2.next, list1

        if list1 or list2:
            cur.next = list1 if list1 else list2

        return dummy.next
