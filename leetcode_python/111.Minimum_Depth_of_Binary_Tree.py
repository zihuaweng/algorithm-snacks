#!/usr/bin/env python3
# coding: utf-8

# Time complexity: O()
# Space complexity: O()

# https://leetcode.com/problems/minimum-depth-of-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        queue = [root]
        depth = 0
        while queue:
            temp = []
            depth += 1
            for q in queue:
                if not q.left and not q.right:
                    return depth
                if q.left:
                    temp.append(q.left)
                if q.right:
                    temp.append(q.right)
            queue = temp
