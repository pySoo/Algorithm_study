# https://leetcode.com/problems/permutations/
"""
- Problem
Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

- Example 1:
Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

- Example 2:
Input: nums = [0,1]
Output: [[0,1],[1,0]]

- Example 3:
Input: nums = [1]
Output: [[1]]
 

- Constraints:
1 <= nums.length <= 6
-10 <= nums[i] <= 10
All the integers of nums are unique.
"""


class Solution(object):
    def permute(self, nums):
        result = []
        prev_n = []

        def dfs(num):
            if len(num) == 0:
                result.append(prev_n[:])

            for n in num:
                next_n = num[:]
                next_n.remove(n)

                prev_n.append(n)
                dfs(next_n)
                prev_n.pop()

        dfs(nums)
        return result
