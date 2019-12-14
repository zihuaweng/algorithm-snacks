#!/usr/bin/env python3
# coding: utf-8

# Time complexity: O()
# Space complexity: O()

# https://leetcode.com/problems/the-maze/

class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:

        # 0 0 1 0 0
        # 0 0 0 0 0
        # 0 0 0 1 0
        # 1 1 0 1 1
        # 0 0 0 0 0

        m = len(maze)
        n = len(maze[0])
        visited = set()
        visited.add(tuple(start))
        queue = [start]
        # print(queue)
        for x, y in queue:
            for _x, _y in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                new_x = x
                new_y = y
                while 0 <= new_x + _x < m and 0 <= new_y + _y < n and maze[new_x + _x][new_y + _y] == 0:
                    new_x = new_x + _x
                    new_y = new_y + _y

                if new_x == destination[0] and new_y == destination[1]:
                    return True
                if (new_x, new_y) not in visited:
                    visited.add((new_x, new_y))
                    queue.append((new_x, new_y))
        return False
