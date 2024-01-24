'''
https://leetcode.com/problems/maximum-subarray

53. Maximum Subarray
Medium

Given an integer array nums, find the
subarray
 with the largest sum, and return its sum.



Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.
Example 2:

Input: nums = [1]
Output: 1
Explanation: The subarray [1] has the largest sum 1.
Example 3:

Input: nums = [5,4,-1,7,8]
Output: 23
Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.


Constraints:

1 <= nums.length <= 105
-104 <= nums[i] <= 104


Follow up: If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.
'''
from typing import List
import unittest

class Solution:
    '''
    space: O(1)
    time: O(n)
    '''
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = nums[0]
        current_sum = nums[0]

        for n in nums[1:]:
            current_sum = max(n, current_sum + n)
            max_sum = max(max_sum, current_sum)

        return max_sum


class TestMaxSubArray(unittest.TestCase):
    def setUp(self):
        self.sut = Solution()

    def tearDown(self):
        pass

    def test_one_item_list(self):
        # action
        actual = self.sut.maxSubArray(nums=[1])

        # asserts
        self.assertEqual(actual, 1)

    def test_max_sub_array(self):
        # action
        actual = self.sut.maxSubArray(nums=[1])

        # asserts
        self.assertEqual(actual, 1)
