'''
https://leetcode.com/problems/ransom-note/
383. Ransom Note
Easy
Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.

 

Example 1:

Input: ransomNote = "a", magazine = "b"
Output: false
Example 2:

Input: ransomNote = "aa", magazine = "ab"
Output: false
Example 3:

Input: ransomNote = "aa", magazine = "aab"
Output: true
 

Constraints:

1 <= ransomNote.length, magazine.length <= 105
ransomNote and magazine consist of lowercase English letters.
'''
import unittest

class Solution(object):
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        frequency = [0] * 26
        
        for m in magazine:
            frequency[ord(m.lower()) - ord('a')] += 1
            
        for r in ransomNote:
            frequency[ord(r.lower()) - ord('a')] -= 1
            
            if frequency[ord(r.lower()) - ord('a')] < 0:
                return False
            
        return True



class TestCanConstruct(unittest.TestCase):
    def setUp(self):
        self.sut = Solution()

    def tearDown(self):
        pass

    def test_empty_magazine_and_empty_note(self):
        # action
        actual = self.sut.canConstruct(ransomNote='', magazine='')

        # asserts
        self.assertEqual(actual, True)

    def test_empty_note(self):
        # action
        actual = self.sut.canConstruct(ransomNote='', magazine='abc')

        # asserts
        self.assertEqual(actual, True)

    def test_insufficient_frequencies(self):
        # action
        actual = self.sut.canConstruct(ransomNote='aa', magazine='abc')

        # asserts
        self.assertEqual(actual, False)

    def test_sufficient_frequencies(self):
        # action
        actual = self.sut.canConstruct(ransomNote='aa', magazine='aabc')

        # asserts
        self.assertEqual(actual, True)