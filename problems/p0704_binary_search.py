'''
https://leetcode.com/problems/binary-search/
704. Binary Search
Easy
Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4
Example 2:

Input: nums = [-1,0,3,5,9,12], target = 2
Output: -1
Explanation: 2 does not exist in nums so return -1
 

Constraints:

1 <= nums.length <= 104
-104 < nums[i], target < 104
All the integers in nums are unique.
nums is sorted in ascending order.
'''

from typing import List
import unittest


class Solution:
    '''
    space: O(1)
    time: O(logn)
    '''
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1
        
        while low <= high:
            mid = (low + high) // 2
            
            if nums[mid] == target:
                return mid 
            
            if nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        
        return -1




class TestSearch(unittest.TestCase):
    def setUp(self):
        self.sut = Solution()

    def tearDown(self):
        pass

    def test_empty_list(self):
        # action
        actual = self.sut.search(nums=[], target=1)

        # asserts
        self.assertEqual(actual, -1)

    def test_not_in_list(self):
        # action
        actual = self.sut.search(nums=[2,3], target=1)

        # asserts
        self.assertEqual(actual, -1)

    def test_one_item_in_list(self):
        # action
        actual = self.sut.search(nums=[5], target=5)

        # asserts
        self.assertEqual(actual, 0)

    def test_duplicates(self):
        # action
        actual = self.sut.search(nums=[1, 5, 5], target=5)

        # asserts
        self.assertEqual(actual, 1)

    def test_result_is_last_item(self):
        # action
        actual = self.sut.search(nums=[1, 3, 5], target=5)

        # asserts
        self.assertEqual(actual, 2)