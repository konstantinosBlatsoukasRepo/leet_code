class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        if len(s) == 1:
            return False

        left_parentheses = []
        for i in range(len(s)):
            current_parentheses = s[i]
            if current_parentheses in [')', ']', '}'] and len(left_parentheses) == 0:
                return False

            if current_parentheses == ')':
                popped = left_parentheses.pop()
                if popped != '(':
                    return False
            elif current_parentheses == ']':
                popped = left_parentheses.pop()
                if popped != '[':
                    return False
            elif current_parentheses == '}':
                popped = left_parentheses.pop()
                if popped != '{':
                    return False
            else:
                left_parentheses.append(current_parentheses)

        if len(left_parentheses) > 0:
            return False

        return True
