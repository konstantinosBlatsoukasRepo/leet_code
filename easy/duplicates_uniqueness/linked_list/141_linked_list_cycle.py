# slow fast is better solution

    # def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        
    #     if  head == None or head.next :
    #         return 0
        
        
    #     slow = head 
    #     fast = head
        
        
    #     while fast != None and fast.next != None:
            
    #         slow = slow.next 
    #         fast = fast.next.next 
            
    #         if slow == fast :
                
    #             return 1
    #     return 0


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        return self.hasCycleInner(head, [])


    def hasCycleInner(self, head, seen):
        if head is None:
            return False

        if head.next in seen:
            return True

        seen.append(head)
        return self.hasCycleInner(head.next, seen)

