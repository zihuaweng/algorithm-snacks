#!/usr/bin/env python3
# coding: utf-8

# Time complexity: O(n)
# Space complexity: O()

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        res = []

        def pre_order(node):
            if node:
                res.append(str(node.val))
                pre_order(node.left)
                pre_order(node.right)
            else:
                res.append('#')

        pre_order(root)

        return ' '.join(res)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        vals = iter(data.split())   # 也可以写成一个queue

        def pre_order():
            val = next(vals)
            if val == '#':
                return None
            node = TreeNode(int(val))
            node.left = pre_order()
            node.right = pre_order()
            return node

        root = pre_order()

        return root

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))