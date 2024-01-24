'''
739. Daily Temperatures
Medium

Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.



Example 1:

Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]
Example 2:

Input: temperatures = [30,40,50,60]
Output: [1,1,1,0]
Example 3:

Input: temperatures = [30,60,90]
Output: [1,1,0]


Constraints:

1 <= temperatures.length <= 105
30 <= temperatures[i] <= 100
'''
from typing import List
from collections import deque
import unittest

class Solution:
    '''
    space: O(n)
    time: O(n)
    '''
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        result = [0] * n
        stack = deque()

        for i in range(n):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                last_index = stack.pop()
                result[last_index] = i - last_index

            stack.append(i)

        return result



class TestDailyTemperatures(unittest.TestCase):
    def setUp(self):
        self.sut = Solution()

    def tearDown(self):
        pass

    def test_empty_list(self):
        # action
        actual = self.sut.dailyTemperatures(temperatures=[])

        # asserts
        self.assertEqual(actual, [])

    def test_dailyTemperatures(self):
        # action
        actual = self.sut.dailyTemperatures(temperatures=[73,74,75,71,69,72,76,73])

        # asserts
        self.assertEqual(actual, [1, 1, 4, 2, 1, 1, 0, 0])
