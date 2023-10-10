'''
https://leetcode.com/problems/merge-two-sorted-lists/
21. Merge Two Sorted Lists
Easy
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

 

Example 1:


Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]
Example 2:

Input: list1 = [], list2 = []
Output: []
Example 3:

Input: list1 = [], list2 = [0]
Output: [0]
 

Constraints:

The number of nodes in both lists is in the range [0, 50].
-100 <= Node.val <= 100
Both list1 and list2 are sorted in non-decreasing order.
'''

import unittest
from typing import Optional

class ListNode:
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


class Solution:
    '''
    space: O(1)
    time: O(m+n)
    '''
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode(0)
        ptr = head

        while list1 and list2:
            if list1.val <= list2.val:
                ptr.next = list1
                list1 = list1.next
            else:
                ptr.next = list2
                list2 = list2.next
            
            ptr = ptr.next

        
        if list1 is None:
            ptr.next = list2
        elif list2 is None:
            ptr.next = list1
            

        return head.next




class TestMergeTwoSortedLists(unittest.TestCase):
    def setUp(self):
        self.sut = Solution()

    def tearDown(self):
        pass

    def test_empty_lists(self):
        # action
        actual = self.sut.mergeTwoLists(list1=None, list2=None)

        # asserts
        self.assertEqual(actual, None)

    def test_one_empty_list(self):
        # action
        actual = self.sut.mergeTwoLists(list1=None, list2=ListNode(10))

        # asserts
        self.assertEqual(actual, ListNode(10))

    def test_two_list(self):
        # action
        actual = self.sut.mergeTwoLists(list1=ListNode(
            1,
            ListNode(
                3,
                ListNode(5)
            )
        ), list2=ListNode(
            2,
            ListNode(
                4,
                ListNode(6)
            )
        ))

        # asserts
        self.assertEqual(actual, ListNode(
            1,
            ListNode(
                2,
                ListNode(
                    3,
                    ListNode(
                        4,
                        ListNode(
                            5,
                            ListNode(
                                6
                            )
                        )
                    )
                )
            )
        ))