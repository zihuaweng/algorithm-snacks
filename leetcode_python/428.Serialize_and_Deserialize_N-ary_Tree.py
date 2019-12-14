#!/usr/bin/env python3
# coding: utf-8

# Time complexity: O()
# Space complexity: O()

# https://leetcode.com/problems/serialize-and-deserialize-n-ary-tree/

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
        data = []

        def helper(root):
            if not root:
                data.append('#')
                return
            data.append(str(root.val))
            helper(root.left)
            helper(root.right)

        helper(root)
        return ','.join(data)


    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None
        queue = collections.deque(data.split(','))

        def helper(queue):
            if not queue:
                return None
            tmp = queue.popleft()
            if tmp == '#':
                return None
            root = TreeNode(int(tmp))
            root.left = helper(queue)
            root.right = helper(queue)
            return root

        return helper(queue)


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))