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
    def countNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        return self.countNodes(root.left) + self.countNodes(root.right) + 1

    # 简化完全树的计算
    def countNodes2(self, root: TreeNode) -> int:
        height_l = height_r = 0
        left = right = root
        while left:
            height_l += 1
            left = left.left

        while right:
            height_r += 1
            right = right.right

        if height_l == height_r:
            return (1 << height_l) - 1  # 完全树的节点个数计算： 2^h - 1
        else:
            return self.countNodes(root.left) + self.countNodes(root.right) + 1