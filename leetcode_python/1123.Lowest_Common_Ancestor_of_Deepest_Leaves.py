#!/usr/bin/env python3
# coding: utf-8

# Time complexity: O()
# Space complexity: O()


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lcaDeepestLeaves(self, root: TreeNode) -> TreeNode:

        #            depth
        #   3  0        0
        #      /\
        # (3) 1  2  (2) 1
        #    /
        #   3           2
        #               3   (max)

        if not root:
            return []

        self.loc = None
        self.depth = 0
        self.dfs(root, 0)
        return self.loc

    def dfs(self, node, depth):
        self.depth = max(self.depth, depth)
        if not node:
            return depth
        left = self.dfs(node.left, depth + 1)
        right = self.dfs(node.right, depth + 1)
        if left == right == self.depth:
            self.loc = node
        return max(left, right)
