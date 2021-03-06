# https://leetcode.com/problems/valid-palindrome/
"""
- Problem
Given a string s, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

- Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.

- Example 2:

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.
 

- Constraints:
1 <= s.length <= 2 * 105
s consists only of printable ASCII characters.
"""
from collections import deque


class Solution(object):
    def isPalindrome(self, s):
        strs = deque()

        for char in s:
            if char.isalnum():
                strs.append(char.lower())

        while len(strs) > 1:
            if strs.popleft() != strs.pop():
                return False
        return True
