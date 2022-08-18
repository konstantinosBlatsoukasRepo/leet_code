# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# class Solution:
#     def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         seen = set()

#         current_node = head
#         while current_node:
#             if current_node in seen:
#                 return current_node
#             else:
#                 seen.add(current_node)
#                 current_node = current_node.next
#         return None


from collections import Counter


from collections import Counter
my_counter = Counter("abc")



print(list(my_counter.values())[0])

result = 0
one_found = False
for freq in my_counter.values():
    if freq % 2 == 0:
        result += freq
    elif freq == 1 and  not one_found:
        result += freq


