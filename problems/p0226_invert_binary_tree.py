'''
https://leetcode.com/problems/invert-binary-tree/

226. Invert Binary Tree
Easy
Given the root of a binary tree, invert the tree, and return its root.

 

Example 1:


Input: root = [4,2,7,1,3,6,9]
Output: [4,7,2,9,6,3,1]
Example 2:


Input: root = [2,1,3]
Output: [2,3,1]
Example 3:

Input: root = []
Output: []
 

Constraints:

The number of nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100

'''

from typing import Optional
from typing import List
import unittest



# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right 
        
    def toList(self) -> List:
        arr = []
        TreeNode.toListNode(arr, self)
        return arr
    
    @staticmethod    
    def toListNode(arr: List, root: "TreeNode") -> List:
        if root is None:
            return arr
        
        TreeNode.toListNode(arr, root.left)    
        arr.append(root.val)
        TreeNode.toListNode(arr, root.right)    
        
        
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return None
        
        root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        
        return root
    
    def invertTreeUsingQueue(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return None
        
        queue = [root]
        while queue:
            cur = queue.pop(0)
            cur.left, cur.right = cur.right, cur.left
            if cur.left:
                queue.append(cur.left)
            if cur.right:
                queue.append(cur.right)
        
        return root
    

class TestInvertTree(unittest.TestCase):
    def setUp(self):
        self.sut = Solution()

    def tearDown(self):
        pass

    def test_empty_tree(self):
        # action
        actual = self.sut.invertTree(root=None)

        # asserts
        self.assertEqual(actual, None)

    def test_tree_has_only_root(self):
        # action
        actual = self.sut.invertTree(root=TreeNode(1))

        # asserts
        self.assertEqual(actual.toList(), TreeNode(1).toList())

    def test_tree_unbalanced(self):
        # action
        actual = self.sut.invertTree(root=TreeNode(2, TreeNode(1)))

        # asserts
        self.assertEqual(actual.toList(), TreeNode(2, None, TreeNode(1)).toList())

    def test_tree_balanced(self):
        # action
        actual = self.sut.invertTree(root=TreeNode(2, TreeNode(1), TreeNode(3)))

        # asserts
        self.assertEqual(actual.toList(), TreeNode(2, TreeNode(3), TreeNode(1)).toList())
        
    
    # UsingQueue
    def test_tree_has_only_root_using_queue(self):
        # action
        actual = self.sut.invertTreeUsingQueue(root=TreeNode(1))

        # asserts
        self.assertEqual(actual.toList(), TreeNode(1).toList())

    def test_tree_unbalanced_using_queue(self):
        # action
        actual = self.sut.invertTreeUsingQueue(root=TreeNode(2, TreeNode(1)))

        # asserts
        self.assertEqual(actual.toList(), TreeNode(2, None, TreeNode(1)).toList())

    def test_tree_balanced_using_queue(self):
        # action
        actual = self.sut.invertTreeUsingQueue(root=TreeNode(2, TreeNode(1), TreeNode(3)))

        # asserts
        self.assertEqual(actual.toList(), TreeNode(2, TreeNode(3), TreeNode(1)).toList())