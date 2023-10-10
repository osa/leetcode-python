'''
https://leetcode.com/problems/first-bad-version/

278. First Bad Version
Easy
You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product fails the quality check. Since each version is developed based on the previous version, all the versions after a bad version are also bad.

Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to be bad.

You are given an API bool isBadVersion(version) which returns whether version is bad. Implement a function to find the first bad version. You should minimize the number of calls to the API.

 

Example 1:

Input: n = 5, bad = 4
Output: 4
Explanation:
call isBadVersion(3) -> false
call isBadVersion(5) -> true
call isBadVersion(4) -> true
Then 4 is the first bad version.
Example 2:

Input: n = 1, bad = 1
Output: 1
 

Constraints:

1 <= bad <= n <= 231 - 1
'''
import unittest
from unittest import mock

# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:
def isBadVersion(version: int) -> bool:
    return False


class Solution:
    '''
    space: O(1)
    time: O(logn)
    '''
    def firstBadVersion(self, n: int) -> int:
        left, right  = 1, n
        
        while left <= right:
            mid = (left + right) // 2
            
            if isBadVersion(mid):
                if not (isBadVersion(mid-1)):
                    return mid
                right = mid - 1
            else:
                left = mid + 1
            
        return left
                


class TestFirstBadVersion(unittest.TestCase):
    def setUp(self):
        self.sut = Solution()

    def tearDown(self):
        pass

    def test_n_is_zero(self):
        # action
        actual = self.sut.firstBadVersion(n = 0)

        # asserts
        self.assertEqual(actual, 1)


    @mock.patch('p0278_first_bad_version.isBadVersion')
    def test_n_is_one(self, mock_isBadVersion_call):
        # setup
        def side_effect_isBadVersion(version: int):
            return version == 1
        
        mock_isBadVersion_call.side_effect = side_effect_isBadVersion
        
        # action
        actual = self.sut.firstBadVersion(n = 1)

        # asserts
        self.assertEqual(actual, 1)


    @mock.patch('p0278_first_bad_version.isBadVersion')
    def test_should_find_first_bad_version(self, mock_isBadVersion_call):
        # setup
        def side_effect_isBadVersion(version: int):
            return version == 4
        
        mock_isBadVersion_call.side_effect = side_effect_isBadVersion
        
        # action
        actual = self.sut.firstBadVersion(n = 5)

        # asserts
        self.assertEqual(actual, 4)
