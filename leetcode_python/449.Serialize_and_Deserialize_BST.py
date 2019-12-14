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

class Codec:

    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string.
        """
        data = []

        def helper(root):
            if not root:
                return
            data.append(str(root.val))
            helper(root.left)
            helper(root.right)

        helper(root)
        return ','.join(data)

    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree.
        """
        if not data:
            return None
        queue = collections.deque(data.split(','))

        def helper(queue, max_val, min_val):
            if not queue:
                return None
            tmp = int(queue[0])
            if tmp < min_val or tmp > max_val:
                return None
            tmp = int(queue.popleft())
            root = TreeNode(tmp)
            root.left = helper(queue, tmp, min_val)
            root.right = helper(queue, max_val, tmp)
            return root

        return helper(queue, float('inf'), float('-inf'))

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))