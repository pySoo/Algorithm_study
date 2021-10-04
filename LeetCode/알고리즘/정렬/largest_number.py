# https://leetcode.com/problems/largest-number/submissions/
"""
- Problem
Given a list of non-negative integers nums, arrange them such that they form the largest number.
Note: The result may be very large, so you need to return a string instead of an integer.

- Example 1:
Input: nums = [10,2]
Output: "210"

- Example 2:
Input: nums = [3,30,34,5,9]
Output: "9534330"

- Example 3:
Input: nums = [1]
Output: "1"

- Example 4:
Input: nums = [10]
Output: "10"

- Constraints:

1 <= nums.length <= 100
0 <= nums[i] <= 10^9
"""


class Solution(object):
    def largestNumber(self, nums):
        def to_swap(n1, n2):
            return str(n1) + str(n2) < str(n2) + str(n1)
        i = 1
        while i < len(nums):
            j = i
            while j > 0 and to_swap(nums[j - 1], nums[j]):
                nums[j], nums[j-1] = nums[j-1], nums[j]
                j -= 1
            i += 1

        return str(int(''.join(map(str, nums))))
