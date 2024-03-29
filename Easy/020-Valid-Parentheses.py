"""
    Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

    An input string is valid if:

    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.
    Every close bracket has a corresponding open bracket of the same type.
"""


class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        d = {'(': ')', '{': '}', '[': ']'}
        stack = []
        for i in s:
            if i in d:
                stack.append(i)
            # checks appended open brackets against dictionary pairs
            elif len(stack) == 0 or d[stack.pop()] != i:
                return False
        # handles case where every bracket is open
        return len(stack) == 0


s = "([{})]"
print(Solution().isValid(s))
