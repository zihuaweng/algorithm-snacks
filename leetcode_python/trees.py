#!/usr/bin/env python3
# coding: utf-8

# Time complexity: O()
# Space complexity: O()


def inorderTraversal(self, root: TreeNode) -> List[int]:
    res = []
    if not root:
        return res
    stack = []
    while root or stack:
        while root:
            stack.append(root)
            root = root.left
        root = stack.pop()
        res.append(root.val)
        root = root.right


def preorderTraversal(self, root: TreeNode) -> List[int]:
    if not root:
        return
    res = []
    stack = [root]
    while stack:
        cur = stack.pop()
        res.append(cur.val)
        if cur.right:
            stack.append(cur.right)
        if cur.left:
            stack.append(cur.left)
    return res


def preorderTraversal(self, root: TreeNode) -> List[int]:
    if not root:
        return
    res = []
    stack = [root]
    while stack:
        cur = stack.pop()
        res.append(cur.val)
        if cur.right:
            stack.append(cur.right)
        if cur.left:
            stack.append(cur.left)
    return res