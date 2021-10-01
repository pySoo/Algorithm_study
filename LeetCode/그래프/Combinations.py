# https://leetcode.com/problems/combinations/
"""
- Problem
Given two integers n and k, return all possible combinations of k numbers out of the range [1, n].
You may return the answer in any order.

- Example 1:

Input: n = 4, k = 2
Output:
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]

- Example 2:
Input: n = 1, k = 1
Output: [[1]]

- Constraints:
1 <= n <= 20
1 <= k <= n
"""


class Solution(object):
    def combine(self, n, k):
        results = []

        def dfs(elements, start, k):
            if k == 0:
                results.append(elements[:])

            for i in range(start, n+1):
                elements.append(i)
                dfs(elements, i+1, k-1)
                elements.pop()
        dfs([], 1, k)
