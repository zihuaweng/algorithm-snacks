#!/usr/bin/env python3
# coding: utf-8

# https://leetcode.com/problems/house-robber-iii/

# Time complexity: O()
# Space complexity: O()

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rob(self, root: TreeNode) -> int:
        return max(self.helper(root))

    def helper(self, root):
        if not root:
            return [0, 0]
        left = self.helper(root.left)
        right = self.helper(root.right)
        res = [0, 0]
        res[0] = max(left) + max(right)
        res[1] = root.val + left[0] + right[0]
        return res
