'''
https://leetcode.com/problems/balanced-binary-tree/
110. Balanced Binary Tree
Easy

Given a binary tree, determine if it is 
height-balanced
.

 

Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: true
Example 2:


Input: root = [1,2,2,3,3,null,null,4,4]
Output: false
Example 3:

Input: root = []
Output: true

'''
from typing import Optional
import unittest

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def height(node: Optional[TreeNode]) -> int:
            if node is None:
                return 0
            
            left_height = height(node.left)
            right_height = height(node.right)
            
            if left_height == -1 or right_height == -1 or abs(left_height - right_height) > 1:
                return -1
            
            return max(left_height, right_height) + 1
        
        return height(root) != -1
    
    



class TestIsBalanced(unittest.TestCase):
    def setUp(self):
        self.sut = Solution()

    def tearDown(self):
        pass

    def test_empty_tree(self):
        # action
        actual = self.sut.isBalanced(root=None)

        # asserts
        self.assertEqual(actual, True)        


    def test_unbalanced_tree(self):
        # setup
        root: TreeNode = TreeNode(1, left=TreeNode(0), right=TreeNode(2, TreeNode(9, TreeNode(7))))
        
        # action
        actual = self.sut.isBalanced(root=root)

        # asserts
        self.assertEqual(actual, False)      


    def test_balanced_tree(self):
        # setup
        root: TreeNode = TreeNode(1, left=TreeNode(0), right=TreeNode(2, TreeNode(9)))
        
        # action
        actual = self.sut.isBalanced(root=root)

        # asserts
        self.assertEqual(actual, True)