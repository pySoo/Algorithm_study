# https://leetcode.com/problems/valid-parentheses/
"""
- Problem
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
An input string is valid if:
Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.

- Example 1:
Input: s = "()"
Output: true

- Example 2:
Input: s = "()[]{}"
Output: true

- Example 3:
Input: s = "(]"
Output: false

- Example 4:
Input: s = "([)]"
Output: false

- Example 5:
Input: s = "{[]}"
Output: true
 

- Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.
"""


class Solution(object):
    def isValid(self, s):
        stack = []
        table = {
            ')': '(',
            '}': '{',
            ']': '[',
        }

        for char in s:
            if char not in table:
                stack.append(char)

            elif not stack or table[char] != stack.pop():
                return False
        return len(stack) == 0
