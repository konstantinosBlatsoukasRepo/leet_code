# pop and push more efficient solution , %  and /  operators
class Solution():
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < -2 ** 31 or x > 2 ** 31 - 1 or x == 0:
            return 0

        temp = str(x)
        if str(x)[0] == '-':
            temp = str(x)[1:]

        res = "".join([a for a in temp[::-1]]).lstrip('0')

        if str(x)[0] == '-':
            res = '-' + res

        if int(res) < -2 ** 31 or int(res) > 2 ** 31 - 1 or int(res) == 0:
            return 0

        return res


sol = Solution()


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """


        node = node.next