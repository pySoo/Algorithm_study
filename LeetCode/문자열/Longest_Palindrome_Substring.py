# https://leetcode.com/problems/longest-palindromic-substring/
"""
- Problem
Given a string s, return the longest palindromic substring in s.

- Example 1:
Input: s = "babad"
Output: "bab"
Note: "aba" is also a valid answer.

- Example 2:
Input: s = "cbbd"
Output: "bb"

- Example 3:
Input: s = "a"
Output: "a"

- Example 4:
Input: s = "ac"
Output: "a"
 

- Constraints:
1 <= s.length <= 1000
s consist of only digits and English letters.
"""


class Solution(object):
    def longestPalindrome(self, s):
        def expand(left, right):
            while left >= 0 and right <= len(s) and s[left] == s[right-1]:
                left -= 1
                right += 1
            return s[left + 1:right - 1]
        if len(s) < 2 or s == s[::-1]:
            return s
        result = ''
        for i in range(len(s) - 1):
            result = max(result, expand(i, i+1), expand(i, i+2), key=len)
        return result
