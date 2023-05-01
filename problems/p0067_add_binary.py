'''
https://leetcode.com/problems/add-binary/description/67. Add Binary
Easy
Given two binary strings a and b, return their sum as a binary string.

 

Example 1:

Input: a = "11", b = "1"
Output: "100"
Example 2:

Input: a = "1010", b = "1011"
Output: "10101"
 

Constraints:

1 <= a.length, b.length <= 104
a and b consist only of '0' or '1' characters.
Each string does not contain leading zeros except for the zero itself.

'''
import unittest

class Solution:
    '''
    space : O(max(m,n)) 
    time: O(max(m,n))
    '''
    def addBinary(self, a: str, b: str) -> str:
        if a is None and b is None:
            return '0'
        
        if a is None:
            return b
        
        if b is None:
            return a
        
        a_len = len(a)
        b_len = len(b)
        max_len = max(a_len, b_len)
        buffer = [''] * max_len
        carry = 0
        
        for i in range(max_len):
            x = int(a[a_len-i-1]) if i < a_len else 0
            y = int(b[b_len-i-1]) if i < b_len else 0
            
            buffer[max_len-i-1] = str((x + y + carry) % 2)
            carry = (x + y + carry) // 2
            
            # print(f'curr={buffer[max_len-i-1]}, carry={carry}')
            
        prefix = '' if carry == 0 else '1'
        # print(f'prefix={prefix}, buffer={buffer}')
            
        return prefix + ''.join(buffer)



class TestAddBinary(unittest.TestCase):
    def setUp(self):
        self.sut = Solution()

    def tearDown(self):
        pass

    def test_empty_strings(self):
        # action
        actual = self.sut.addBinary(a=None, b=None)

        # asserts
        self.assertEqual(actual, '0')    

    def test_empty_a(self):
        # action
        actual = self.sut.addBinary(a=None, b='11')

        # asserts
        self.assertEqual(actual, '11')   

    def test_empty_b(self):
        # action
        actual = self.sut.addBinary(a='11', b=None)

        # asserts
        self.assertEqual(actual, '11')   

    def test_even_lengths_no_carry(self):
        # action
        actual = self.sut.addBinary(a='1', b='0')

        # asserts
        self.assertEqual(actual, '1')   

    def test_even_lengths_with_carry(self):
        # action
        actual = self.sut.addBinary(a='1', b='1')

        # asserts
        self.assertEqual(actual, '10') 

    def test_uneven_lengths_no_carry(self):
        # action
        actual = self.sut.addBinary(a='1', b='10')

        # asserts
        self.assertEqual(actual, '11')     

    def test_uneven_lengths_with_carry(self):
        # action
        actual = self.sut.addBinary(a='1', b='11')

        # asserts
        self.assertEqual(actual, '100')     