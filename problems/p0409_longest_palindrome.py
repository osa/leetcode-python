'''
409. Longest Palindrome
Easy
5K
328
Companies
Given a string s which consists of lowercase or uppercase letters, return the length of the longest palindrome that can be built with those letters.

Letters are case sensitive, for example, "Aa" is not considered a palindrome here.



Example 1:

Input: s = "abccccdd"
Output: 7
Explanation: One longest palindrome that can be built is "dccaccd", whose length is 7.
Example 2:

Input: s = "a"
Output: 1
Explanation: The longest palindrome that can be built is "a", whose length is 1.


Constraints:

1 <= s.length <= 2000
s consists of lowercase and/or uppercase English letters only.
'''
from collections import Counter
import unittest

class Solution:
    def longestPalindrome(self, s: str) -> int:
        counter = Counter(s)

        result = 0
        has_odd_length = False

        for cnt in counter.values():
            if result & 1 and cnt & 1:
                cnt = cnt - 1

            result += cnt

        return result



class TestLongestPalindrome(unittest.TestCase):
    def setUp(self):
        self.sut = Solution()

    def tearDown(self):
        pass

    def test_empty_string(self):
        # action
        actual = self.sut.longestPalindrome('')

        # asserts
        self.assertEqual(actual, 0)

    def test_single_character(self):
        # action
        actual = self.sut.longestPalindrome('A')

        # asserts
        self.assertEqual(actual, 1)

    def test_case_sensitive(self):
        # action
        actual = self.sut.longestPalindrome('Aa')

        # asserts
        self.assertEqual(actual, 1)

    def test_all_paired(self):
        # action
        actual = self.sut.longestPalindrome('aabb')

        # asserts
        self.assertEqual(actual, 4)

    def test_all_unpaired(self):
        # action
        actual = self.sut.longestPalindrome('abcd')

        # asserts
        self.assertEqual(actual, 1)
