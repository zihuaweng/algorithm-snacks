#!/usr/bin/env python3
# coding: utf-8

# https://leetcode.com/problems/keys-and-rooms/
# DFS

# Time complexity: O(N+K)
# Space complexity: O(N)

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        opened = set()
        opened.add(0)
        stack = [0]
        while stack:
            cur = stack.pop()
            for i in rooms[cur]:
                if i not in opened:
                    opened.add(i)
                    stack.append(i)
        return True if len(opened) == len(rooms) else False
