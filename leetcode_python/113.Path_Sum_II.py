#!/usr/bin/env python3
# coding: utf-8

# Time complexity: O()
# Space complexity: O()

# https://leetcode.com/problems/path-sum-ii/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root: TreeNode, target: int) -> List[List[int]]:
        self.res = []
        if not root:
            return self.res

        self.dfs(root, target, [])  # todo
        return self.res

    def dfs(self, node, target, temp):
        if not node:
            return
        if not node.left and not node.right and node.val == target:
            self.res.append(temp + [node.val])
            return

        self.dfs(node.left, target - node.val, temp + [node.val])
        self.dfs(node.right, target - node.val, temp + [node.val])
