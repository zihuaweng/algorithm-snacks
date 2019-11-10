#!/usr/bin/env python3
# coding: utf-8

# Time complexity: O()
# Space complexity: O()

# https://leetcode.com/problems/binary-tree-maximum-path-sum/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        self.max_sum = float('-inf')
        if not root:
            return self.max_sum
        self.dfs(root)
        return self.max_sum

    def dfs(self, node):
        if node.left:
            left = max(self.dfs(node.left), 0)
        else:
            left = 0

        if node.right:
            right = max(self.dfs(node.right), 0)
        else:
            right = 0

        cur = node.val + left + right
        self.max_sum = max(self.max_sum, cur)
        return node.val + max(left, right)
