'''
https://leetcode.com/problems/valid-palindrome/
125. Valid Palindrome
Easy

A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

 

Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
Example 2:

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.
Example 3:

Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.
 

Constraints:

1 <= s.length <= 2 * 105
s consists only of printable ASCII characters.


'''
import re
import unittest

class Solution:
    def isPalindrome(self, s: str):
        cleaned = re.sub(r'[^a-zA-Z0-9]+', '', s).lower()
        st = 0
        end = len(cleaned) - 1
        
        while st < end:
            if cleaned[st] != cleaned[end]:
                return False
            
            st += 1
            end -= 1
        
        return True



class TestIsPalindrome(unittest.TestCase):
    def setUp(self):
        self.sut = Solution()

    def tearDown(self):
        pass

    def test_empty_string(self):
        # action
        actual = self.sut.isPalindrome(s='')

        # asserts
        self.assertEqual(actual, True)

    def test_ignore_case(self):
        # action
        actual = self.sut.isPalindrome(s='A1a')

        # asserts
        self.assertEqual(actual, True)

    def test_ignore_non_alpha_numeric_characters(self):
        # action
        actual = self.sut.isPalindrome(s='A!$)+_a')

        # asserts
        self.assertEqual(actual, True)

    def test_non_palindrome(self):
        # action
        actual = self.sut.isPalindrome(s='A3')

        # asserts
        self.assertEqual(actual, False)