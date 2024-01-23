'''
https://leetcode.com/problems/insert-interval/

57. Insert Interval
Medium

You are given an array of non-overlapping intervals intervals where intervals[i] = [starti, endi] represent the start and the end of the ith interval and intervals is sorted in ascending order by starti. You are also given an interval newInterval = [start, end] that represents the start and end of another interval.

Insert newInterval into intervals such that intervals is still sorted in ascending order by starti and intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).

Return intervals after the insertion.



Example 1:

Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]
Example 2:

Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].


Constraints:

0 <= intervals.length <= 104
intervals[i].length == 2
0 <= starti <= endi <= 105
intervals is sorted by starti in ascending order.
newInterval.length == 2
0 <= start <= end <= 105


'''

from typing import List
import unittest


class Solution:
    '''
    space: O(n)
    time: O(n)
    '''
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        merged_intervals = []

        if len(newInterval) != 2:
            return intervals

        for i in range(len(intervals)):
            interval = intervals[i]

            if newInterval[1] < interval[0]:
                return merged_intervals + [newInterval] + intervals[i:]

            if newInterval[0] > interval[1]:
                merged_intervals.append(interval)

            else: # expand new interval
                newInterval = [
                    min(newInterval[0], interval[0]),
                    max(newInterval[1], interval[1]),
                ]

        merged_intervals.append(newInterval)


        return merged_intervals

class TestInsertInterval(unittest.TestCase):
    def setUp(self):
        self.sut = Solution()

    def tearDown(self):
        pass

    def test_empty_interval_and_empty_new_interval(self):
        # action
        actual = self.sut.insert(intervals=[], newInterval=[])

        # asserts
        self.assertEqual(actual, [])

    def test_empty_interval(self):
        # action
        actual = self.sut.insert(intervals=[], newInterval=[1,2])

        # asserts
        self.assertEqual(actual, [[1,2]])

    def test_empty_new_interval(self):
        # action
        actual = self.sut.insert(intervals=[[1,2]], newInterval=[])

        # asserts
        self.assertEqual(actual, [[1,2]])
        self.assertEqual(actual, [[1,2]])

    def test_non_overlap_at_end(self):
        # action
        actual = self.sut.insert(intervals=[[1,2]], newInterval=[3, 4])

        # asserts
        self.assertEqual(actual, [[1,2],[3, 4]])

    def test_non_overlap_at_start(self):
        # action
        actual = self.sut.insert(intervals=[[3,4]], newInterval=[1, 2])

        # asserts
        self.assertEqual(actual, [[1,2],[3, 4]])

    def test_non_overlap_at_middle(self):
        # action
        actual = self.sut.insert(intervals=[[1, 2], [5,6]], newInterval=[3,4])

        # asserts
        self.assertEqual(actual, [[1,2],[3, 4],[5, 6]])

    def test_overlap(self):
        # action
        actual = self.sut.insert(intervals=[[1, 2], [5,6]], newInterval=[2,5])

        # asserts
        self.assertEqual(actual, [[1, 6]])