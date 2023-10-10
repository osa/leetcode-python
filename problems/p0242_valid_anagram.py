'''
https://leetcode.com/problems/valid-anagram/
242. Valid Anagram
Easy
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
 

Constraints:

1 <= s.length, t.length <= 5 * 104
s and t consist of lowercase English letters.
 

'''
import unittest

class Solution(object):
    '''
    space: O(1)
    time: O(n)
    '''
    def isAnagram(self, s: str, t: str):
        if len(s) != len(t):
            return False
        
        frequency = [0] * 26
        
        for i, c in enumerate(s):
            frequency[ord(c.lower()) - ord('a')] += 1
            frequency[ord(t[i].lower()) - ord('a')] -= 1
        
        return frequency == [0] * 26



class TestIsAnagram(unittest.TestCase):
    def setUp(self):
        self.sut = Solution()

    def tearDown(self):
        pass

    def test_empty_string(self):
        # action
        actual = self.sut.isAnagram(s='', t='')

        # asserts
        self.assertEqual(actual, True)

    def test_different_lengths(self):
        # action
        actual = self.sut.isAnagram(s='ab', t='a')

        # asserts
        self.assertEqual(actual, False)

    def test_non_anagram(self):
        # action
        actual = self.sut.isAnagram(s='a', t='b')

        # asserts
        self.assertEqual(actual, False)

    def test_valid_anagram(self):
        # action
        actual = self.sut.isAnagram(s='ab', t='ba')

        # asserts
        self.assertEqual(actual, True)