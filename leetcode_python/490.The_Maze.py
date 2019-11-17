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
        visited = [[False] * n for _ in range(m)]
        visited[start[0]][start[1]] = True
        queue = collections.deque([])
        queue.append(start)
        # print(queue)
        while queue:
            x, y = queue.popleft()
            for _x, _y in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                new_x = x
                new_y = y
                while 0 <= new_x + _x < m and 0 <= new_y + _y < n and maze[new_x + _x][new_y + _y] == 0:
                    new_x = new_x + _x
                    new_y = new_y + _y

                if new_x == destination[0] and new_y == destination[1]:
                    return True
                if not visited[new_x][new_y]:
                    visited[new_x][new_y] = True
                    queue.append((new_x, new_y))
        return False
