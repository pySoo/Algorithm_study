# https://leetcode.com/problems/longest-substring-without-repeating-characters/
"""
- Problem
Given a string s, find the length of the longest substring without repeating characters.

- Example 1:
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

- Example 2:
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

- Example 3:
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

- Example 4:
Input: s = ""
Output: 0
 

- Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.
"""


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        used = {}
        max_length = start = 0
        for idx, char in enumerate(s):
            if char in used and start <= used[char]:
                start = used[char] + 1
                print(char, idx, start)
            else:
                max_length = max(max_length, idx - start + 1)

            used[char] = idx
        return max_length
