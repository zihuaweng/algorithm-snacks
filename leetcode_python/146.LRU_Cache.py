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
        # self._print_node()
        if key in self.ele:
            value = self.ele[key].val
            self._remove(self.ele[key])
            self._add(key, value)
            return self.ele[key].val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        # self._print_node()
        if key in self.ele:
            self._remove(self.ele[key])

        elif len(self.ele) == self.capacity:
            first = self.head.next
            self._remove(first)

        self._add(key, value)

    def _add(self, key, value):
        node = Node(key, value)
        p = self.tail.pre
        p.next = node
        node.pre = p
        node.next = self.tail
        self.tail.pre = node
        self.ele[key] = node

    def _remove(self, node):
        p = node.pre
        p.next = node.next
        node.next.pre = p
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