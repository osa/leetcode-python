'''
https://leetcode.com/problems/two-sum/

1. Two Sum
Easy
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

 

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
 

Constraints:

2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.
 

Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?


'''
from typing import List
import unittest


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = {}

        for i, num in enumerate(nums):
            temp = target - num
            if temp in result:
                return [result[temp], i]
            result.update({num: i})

        return []



class TestTwoSum(unittest.TestCase):
    def setUp(self):
        self.sut = Solution()

    def tearDown(self):
        pass

    def test_empty_list(self):
        # action
        actual = self.sut.twoSum(nums=[], target=10)

        # asserts
        self.assertEqual(actual, [])

    def test_result_does_not_exist(self):
        # action
        actual = self.sut.twoSum([1, 2], 1)

        # asserts
        self.assertEqual(actual, [])

    def test_finds_indices(self):
        # action
        actual = self.sut.twoSum([2, 7, 11, 15], 9)

        # asserts
        self.assertEqual(actual, [0, 1])