#!/usr/bin/env python3
# coding: utf-8

# https://leetcode.com/problems/path-sum-iii/

# Time complexity: O(n)
# Space complexity: O(n*n)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        if not root:
            return 0
        return self.dfs(root, sum) + self.pathSum(root.left, sum) + self.pathSum(root.right, sum)

    def dfs(self, node, target):
        if not node:
            return 0
        target -= node.val
        res = 1 if target == 0 else 0
        return res + self.dfs(node.left, target) + self.dfs(node.right, target)

