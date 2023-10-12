'''
338. Counting Bits
Easy

Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), ans[i] is the number of 1's in the binary representation of i.


Example 1:

Input: n = 2
Output: [0,1,1]
Explanation:
0 --> 0
1 --> 1
2 --> 10
Example 2:

Input: n = 5
Output: [0,1,1,2,1,2]
Explanation:
0 --> 0
1 --> 1
2 --> 10
3 --> 11
4 --> 100
5 --> 101


Constraints:

0 <= n <= 105


Follow up:

It is very easy to come up with a solution with a runtime of O(n log n). Can you do it in linear time O(n) and possibly in a single pass?
Can you do it without using any built-in function (i.e., like __builtin_popcount in C++)?
'''

from typing import List
import unittest


class Solution:
    '''
    space: O(n)
    time: O(n)
    '''
    def countBits(self, n: int) -> List[int]:
        result = [0] * (n + 1)

        for i in range(1, n + 1):
            result[i] = result[i >> 1] + (i & 1)

        return result



class TestCountBits(unittest.TestCase):
    def setUp(self):
        self.sut = Solution()

    def tearDown(self):
        pass

    def test_number(self):
        test_cases = {
            0: [0],
            1: [0, 1],
            5: [0, 1, 1, 2, 1, 2],
        }

        for n in test_cases.keys():
            # action
            actual = self.sut.countBits(n)

            # asserts
            self.assertListEqual(actual, test_cases[n])
            self.assertEqual(len(actual), n + 1)
