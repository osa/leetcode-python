'''
https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/
235. Lowest Common Ancestor of a Binary Search Tree
Medium
Given a binary search tree (BST), find the lowest common ancestor (LCA) node of two given nodes in the BST.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

 

Example 1:


Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
Output: 6
Explanation: The LCA of nodes 2 and 8 is 6.
Example 2:


Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
Output: 2
Explanation: The LCA of nodes 2 and 4 is 2, since a node can be a descendant of itself according to the LCA definition.
Example 3:

Input: root = [2,1], p = 2, q = 1
Output: 2
 

Constraints:

The number of nodes in the tree is in the range [2, 105].
-109 <= Node.val <= 109
All Node.val are unique.
p != q
p and q will exist in the BST.
'''

import unittest

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right
        


class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:  
        ptr = root
        
        while ptr is not None:
            if p.val < ptr.val and q.val < ptr.val:
                ptr = ptr.left
            elif p.val > ptr.val and q.val > ptr.val:
                ptr = ptr.right
            else:
                return ptr
        
        return ptr


class TestSearch(unittest.TestCase):
    def setUp(self):
        self.sut = Solution()

    def tearDown(self):
        pass

    def test_empty_tree(self):
        # action
        actual = self.sut.lowestCommonAncestor(root=None, p=TreeNode(1), q=TreeNode(2))

        # asserts
        self.assertEqual(actual, None)


    def test_root_is_common_ancestor(self):
        # setup
        root: TreeNode = TreeNode(1, left=TreeNode(0), right=TreeNode(2))
        
        # action
        actual = self.sut.lowestCommonAncestor(root=root, p=TreeNode(0), q=TreeNode(2))

        # asserts
        self.assertEqual(actual, root)
        

    def test_find(self):
        # setup
        q: TreeNode = TreeNode(4, TreeNode(3), TreeNode(5))
        p: TreeNode = TreeNode(2, left=TreeNode(0), right=q)
        root: TreeNode = TreeNode(6, left=p, right=TreeNode(8, TreeNode(7), TreeNode(9)))
        
        # action
        actual = self.sut.lowestCommonAncestor(root=root, p=TreeNode(2), q=TreeNode(4))

        # asserts
        self.assertEqual(actual.val, 2)
      