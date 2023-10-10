'''
169. Majority Element
Easy
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.



Example 1:

Input: nums = [3,2,3]
Output: 3
Example 2:

Input: nums = [2,2,1,1,1,2,2]
Output: 2


Constraints:

n == nums.length
1 <= n <= 5 * 104
-109 <= nums[i] <= 109


Follow-up: Could you solve the problem in linear time and in O(1) space?
'''

from typing import List
from collections import Counter
import unittest

class Solution:
    '''
    space: O(n)
    time: O(n)
    '''
    def majorityElement(self, nums: List[int]) -> int:
        counter = Counter(nums)
        cutoff = len(nums) // 2

        for key in counter.keys():
            if counter[key] > cutoff:
                return key

        pass # should never reach here

    '''
    Boyer-Moore Voting Algorithm
    space: O(1)
    time: O(n)
    '''
    def majorityElement_optimized(self, nums: List[int]) -> int:
        candidate = None
        count = 0

        for i in nums:
            if count == 0:
                candidate = i

            count += 1 if candidate == i else -1

        return candidate



class TestMajorityElement(unittest.TestCase):
    def setUp(self):
        self.sut = Solution()

    def tearDown(self):
        pass

    def test_single_element(self):
        # action
        actual = self.sut.majorityElement([1])

        # asserts
        self.assertEqual(actual, 1)

    def test_single_odd_lenth(self):
        # action
        actual = self.sut.majorityElement([1, 2, 1])

        # asserts
        self.assertEqual(actual, 1)

    def test_single_even_lenth(self):
        # action
        actual = self.sut.majorityElement([1, 2, 1, 1])

        # asserts
        self.assertEqual(actual, 1)

    def test_single_element_optimized(self):
        # action
        actual = self.sut.majorityElement_optimized([1])

        # asserts
        self.assertEqual(actual, 1)

    def test_single_odd_lenth_optimized(self):
        # action
        actual = self.sut.majorityElement_optimized([1, 2, 1])

        # asserts
        self.assertEqual(actual, 1)

    def test_single_even_lenth_optimized(self):
        # action
        actual = self.sut.majorityElement_optimized([1, 2, 1, 1])

        # asserts
        self.assertEqual(actual, 1)
