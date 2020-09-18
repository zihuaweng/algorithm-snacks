#!/usr/bin/env python3
# coding: utf-8

# https://leetcode.com/problems/lru-cache/
# 使用双向链表

# 另一种方法使用OrderedDict


# Time complexity: O()
# Space complexity: O()

class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.pre = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.ele = dict()
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.pre = self.head

    def get(self, key: int) -> int:
        if key in self.ele:
            node = self.ele[key]
            self._remove(node)
            self._add(node)
            return node.val

        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.ele:
            self._remove(self.ele[key])
        elif len(self.ele) == self.capacity:
            self._remove(self.head.next)
        node = Node(key, value)
        self._add(node)

    def _add(self, node):
        last = self.tail.pre
        last.next = node
        node.pre = last
        node.next = self.tail
        self.tail.pre = node
        self.ele[node.key] = node

    def _remove(self, node):
        pre = node.pre
        pre.next = node.next
        node.next.pre = pre
        del self.ele[node.key]

    def _print_node(self):
        head = self.head
        res = []
        while head is not None:
            res.append(head.key)
            head = head.next

        print(res)

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)