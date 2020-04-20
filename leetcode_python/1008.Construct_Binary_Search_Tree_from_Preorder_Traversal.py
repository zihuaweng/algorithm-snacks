#!/usr/bin/env python3
# coding: utf-8

# Time complexity: O()
# Space complexity: O()

# https://leetcode.com/problems/construct-binary-search-tree-from-preorder-traversal/
# refer to java!

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        if not preorder:
            return None
        val = preorder[0]
        idx = 1
        while idx < len(preorder) and preorder[idx] < val:
            idx += 1
        node = TreeNode(val)
        node.left = self.bstFromPreorder(preorder[1:idx])
        node.right = self.bstFromPreorder(preorder[idx:])
        return node
