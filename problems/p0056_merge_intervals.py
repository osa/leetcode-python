'''
https://leetcode.com/problems/merge-intervals/
56. Merge Intervals
Medium

Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.


Example 1:

Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].
Example 2:

Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.


Constraints:

1 <= intervals.length <= 104
intervals[i].length == 2
0 <= starti <= endi <= 104
'''


from typing import List
import unittest
class Solution:
    '''
    space: O(n)
    time: O(n + nlogn)
    '''
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        result = []

        for interval in intervals:
            if not result or interval[0] > result[-1][1]:
                result.append(interval)
            else:
                result[-1][1] = max(result[-1][1], interval[1])

        return result

class TestMerge(unittest.TestCase):
    def setUp(self):
        self.sut = Solution()

    def tearDown(self):
        pass

    def test_empty_list(self):
        # action
        actual = self.sut.merge(intervals=[])

        # asserts
        self.assertEqual([], actual)

    def test_empty_merge(self):
        # action
        actual = self.sut.merge(intervals=[[1,3],[2,6],[8,10],[15,18]])

        # asserts
        self.assertEqual([[1,6],[8,10],[15,18]], actual)

