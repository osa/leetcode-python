'''
https://leetcode.com/problems/contains-duplicate/

217. Contains Duplicate
Easy
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

 

Example 1:

Input: nums = [1,2,3,1]
Output: true
Example 2:

Input: nums = [1,2,3,4]
Output: false
Example 3:

Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true
 

Constraints:

1 <= nums.length <= 105
-109 <= nums[i] <= 109
'''

from typing import List
import unittest

class Solution:
    '''
    space: O(n)
    time: O(nlogn)
    '''
    def containsDuplicate(self, nums: List[int]) -> bool:
        found = set()
        
        for i in nums:
            if i in found:
                return True
            
            found.add(i)
        
        return False


class TestContainsDuplicate(unittest.TestCase):
    def setUp(self):
        self.sut = Solution()

    def tearDown(self):
        pass

    def test_empty_list(self):
        # action
        actual = self.sut.containsDuplicate(nums=[])

        # asserts
        self.assertEqual(actual, False)

    def test_no_duplicates(self):
        # action
        actual = self.sut.containsDuplicate(nums=[1, 2, 3])

        # asserts
        self.assertEqual(actual, False)

    def test_has_duplicates(self):
        # action
        actual = self.sut.containsDuplicate(nums=[1, 1, 3])

        # asserts
        self.assertEqual(actual, True)