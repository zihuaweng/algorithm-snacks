#!/usr/bin/env python3
# coding: utf-8

# https://leetcode.com/problems/campus-bikes-ii/

# Time complexity: O()
# Space complexity: O()


class Solution:
    # 简单dfs需要n!计算， TLE
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> int:

        self.workers = workers
        self.bikes = bikes
        self.min = float('inf')
        n = len(bikes)
        visited = [False] * n
        self.dfs(0, visited, 0)
        return self.min

    def dfs(self, index, visited, min_dis):
        if index == len(self.workers):
            self.min = min(self.min, min_dis)
            return

        if min_dis >= self.min:
            return

        for i in range(len(visited)):
            if not visited[i]:
                visited[i] = True
                self.dfs(index + 1, visited, min_dis + self.dist(self.workers[index], self.bikes[i]))
                visited[i] = False

    def dist(self, w, b):
        return abs(w[0] - b[0]) + abs(w[1] - b[1])


# 和上一个一样，但是使用了位运算dp
# https://www.youtube.com/watch?v=nyOE2x5vTUk&t=640s
# 这里有具体的位运算解释
class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> int:

        self.workers = workers
        self.bikes = bikes
        n = len(bikes)
        dp = [0] * (1 << n)
        return self.dfs(0, 0, dp)

    def dfs(self, index, state, dp):
        if index == len(self.workers):
            return 0
        if dp[state] != 0:
            return dp[state]

        min_dis = float('inf')
        for i in range(len(self.bikes)):
            if state & (1 << i) == 0:
                min_dis = min(min_dis,
                              self.dist(index, i) + self.dfs(index + 1, state | (1 << i), dp))
        dp[state] = min_dis
        return min_dis

    def dist(self, i, j):
        return abs(self.workers[i][0] - self.bikes[j][0]) + abs(self.workers[i][1] - self.bikes[j][1])


# 使用 priorityqueue , 类似Djikstra's
# https://leetcode.com/problems/campus-bikes-ii/discuss/303422/Python-Priority-Queue
class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> int:

        def dist(i, j):
            return abs(workers[i][0] - bikes[j][0]) + abs(workers[i][1] - bikes[j][1])

        h = [[0, 0, 0]]
        seen = set()
        while True:
            cost, i, token = heapq.heappop(h)
            if (i, token) not in seen:
                seen.add((i, token))
                if i == len(workers):
                    return cost
                for j in range(len(bikes)):
                    if token & (1 << j) == 0:
                        heapq.heappush(h, [cost + dist(i, j), i + 1, token | (1 << j)])

