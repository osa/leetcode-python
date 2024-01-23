'''
https://leetcode.com/problems/string-to-integer-atoi/

8. String to Integer (atoi)
Medium

Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer (similar to C/C++'s atoi function).

The algorithm for myAtoi(string s) is as follows:

Read in and ignore any leading whitespace.
Check if the next character (if not already at the end of the string) is '-' or '+'. Read this character in if it is either. This determines if the final result is negative or positive respectively. Assume the result is positive if neither is present.
Read in next the characters until the next non-digit character or the end of the input is reached. The rest of the string is ignored.
Convert these digits into an integer (i.e. "123" -> 123, "0032" -> 32). If no digits were read, then the integer is 0. Change the sign as necessary (from step 2).
If the integer is out of the 32-bit signed integer range [-231, 231 - 1], then clamp the integer so that it remains in the range. Specifically, integers less than -231 should be clamped to -231, and integers greater than 231 - 1 should be clamped to 231 - 1.
Return the integer as the final result.
Note:

Only the space character ' ' is considered a whitespace character.
Do not ignore any characters other than the leading whitespace or the rest of the string after the digits.
'''
import unittest

INT_MIN = -2 ** 31
INT_MAX = 2 ** 31 - 1

class Solution:
    def myAtoi(self, s: str) -> int:
        total: int = 0
        sign: int = 1
        start_processing: bool = False

        for c in s:
            if not start_processing:
                if c.isdigit():
                    start_processing = True
                    total = total * 10 + int(c)
                elif c == '+':
                    start_processing = True
                elif c == '-':
                    start_processing = True
                    sign = -1
                elif c == ' ':
                    continue
                else:
                    return 0 # Not an integer
            elif c.isdigit():
               total = total * 10 + int(c)
            else:
                break #stop processing

        total *= sign
        total = min(max(total, INT_MIN), INT_MAX)

        return total

class TestAtoi(unittest.TestCase):
    def setUp(self):
        self.sut = Solution()

    def tearDown(self):
        pass

    def test_empty_string(self):
        # action
        actual = self.sut.myAtoi(s=" ")

        # asserts
        self.assertEqual(actual, 0)

    def test_non_numeric_string(self):
        # action
        actual = self.sut.myAtoi(s="abc")

        # asserts
        self.assertEqual(actual, 0)

    def test_only_sign(self):
        # action
        actual = self.sut.myAtoi(s="+")

        # asserts
        self.assertEqual(actual, 0)

    def test_zeroes_space_before_number(self):
        # action
        actual = self.sut.myAtoi(s="000123")

        # asserts
        self.assertEqual(actual, 123)

    def test_white_space_before_number(self):
        # action
        actual = self.sut.myAtoi(s="    123")

        # asserts
        self.assertEqual(actual, 123)

    def test_sign_before_number(self):
        # action
        actual = self.sut.myAtoi(s="-123")

        # asserts
        self.assertEqual(actual, -123)

    def test_too_low_number(self):
        # action
        actual = self.sut.myAtoi(s="-2147483649")

        # asserts
        self.assertEqual(actual, INT_MIN)

    def test_too_high_number(self):
        # action
        actual = self.sut.myAtoi(s="2147483648")

        # asserts
        self.assertEqual(actual, INT_MAX)

    def test_atoi(self):
        # action
        actual = self.sut.myAtoi(s="-1000")

        # asserts
        self.assertEqual(actual, -1000)
