#!/usr/bin/env python3
# coding: utf-8

# Time complexity: O()
# Space complexity: O()

# https://leetcode.com/problems/alien-dictionary/
# 首先构建图
# 打印拓扑结构

class Solution:
    def alienOrder(self, words: List[str]) -> str:
        graph = {}
        in_degree = {}
        self.build_graph(graph, in_degree, words)
        res = self.dfs(graph, in_degree)
        return res

    def build_graph(self, graph, in_degree, words):
        for w in words:            #  这里很重要，否则例子['z', 'z']会报错
            for c in w:
                graph[c] = set()
                in_degree[c] = 0

        for i in range(1, len(words)):
            a = words[i - 1]
            b = words[i]
            idx = 0
            while idx < len(a) and idx < len(b):
                if a[idx] != b[idx]:
                    if b[idx] not in graph[a[idx]]:  # 防止同样组合多次出现
                        graph[a[idx]].add(b[idx])
                        in_degree[b[idx]] += 1
                    break
                idx += 1

    def dfs(self, graph, in_degree):
        res = ''
        queue = [i for i in graph if in_degree[i] == 0]
        for q in queue:
            res += q
            for char in graph[q]:
                in_degree[char] -= 1
                if in_degree[char] == 0:
                    queue.append(char)

        if len(res) == len(graph):
            return res
        else:
            return ""

