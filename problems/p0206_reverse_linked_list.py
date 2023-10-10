'''
https://leetcode.com/problems/reverse-linked-list/
206. Reverse Linked List
Easy

Given the head of a singly linked list, reverse the list, and return the reversed list.

 

Example 1:


Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]
Example 2:


Input: head = [1,2]
Output: [2,1]
Example 3:

Input: head = []
Output: []
 

Constraints:

The number of nodes in the list is the range [0, 5000].
-5000 <= Node.val <= 5000

'''

import unittest

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __eq__(self, __o: object) -> bool:
        if not isinstance(__o, ListNode):
            return False

        self_ptr: ListNode = self
        other_ptr: ListNode = __o

        while self_ptr is not None and other_ptr is not None:
            # print(f'self_ptr={self_ptr.val}, other_ptr={other_ptr.val}')
            if self_ptr.val != other_ptr.val:
                break

            self_ptr = self_ptr.next
            other_ptr = other_ptr.next

        return self_ptr is None and other_ptr is None
        
    def print(self):
        ptr = self
        
        while ptr:
            print(f'{ptr.val}, ', end = '')
            ptr = ptr.next
            
        print('')
        
        

class Solution(object):
    '''
    space: O(1)
    time: O(n)
    '''
    def reverseList(self, head: ListNode) -> ListNode:
        previous_node: ListNode = None
        current_node: ListNode = head
            
        while current_node:
            next_node = current_node.next
            current_node.next = previous_node
            previous_node = current_node
            current_node = next_node
        
        return previous_node
        
 


class TestReverseList(unittest.TestCase):
    def setUp(self):
        self.sut = Solution()

    def tearDown(self):
        pass

    def test_null_list(self):
        # action
        actual = self.sut.reverseList(head=None)

        # asserts
        self.assertEqual(actual, None)   
        

    def test_empty_ist(self):
        # action
        actual = self.sut.reverseList(head=ListNode(1))

        # asserts
        self.assertEqual(actual, ListNode(1))   
        

    def test_list_with_more_than_one_item(self):
        # action
        actual = self.sut.reverseList(head=ListNode(1, ListNode(2)))

        # asserts
        self.assertEqual(actual, ListNode(2, ListNode(1)))
