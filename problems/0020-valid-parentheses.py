'''
https://leetcode.com/problems/valid-parentheses/
20. Valid Parentheses
Easy
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 

Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false
 

Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.
'''
import unittest

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        matches = {
            ')':'(',
            '}':'{',
            ']':'[',
        }

        for _, c in enumerate(s):
            if c in matches.values():
                stack.append(c)
            else:
                if len(stack) == 0:
                    return False

                peek = stack[len(stack) - 1]

                if matches[c] == peek:
                    stack.pop()
                else:
                    return False

        return len(stack) == 0



class TestValidParentheses(unittest.TestCase):
    def setUp(self):
        self.sut = Solution()

    def tearDown(self):
        pass

    def test_empty_string(self):
        # action
        actual = self.sut.isValid(s='')

        # asserts
        self.assertEqual(actual, True)

    def test_non_overlapping(self):
        # action
        actual = self.sut.isValid(s='[]{}()')

        # asserts
        self.assertEqual(actual, True)

    def test_overlapping(self):
        # action
        actual = self.sut.isValid(s='([]{})')

        # asserts
        self.assertEqual(actual, True)

    def test_non_matched_closing(self):
        # action
        actual = self.sut.isValid(s='[]{})')

        # asserts
        self.assertEqual(actual, False)

    def test_non_matched_opening(self):
        # action
        actual = self.sut.isValid(s='[]{')

        # asserts
        self.assertEqual(actual, False)