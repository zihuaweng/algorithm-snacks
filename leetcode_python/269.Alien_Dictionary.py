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
        in_degree = [0] * 26
        self.build_graph(graph, in_degree, words)
        res = self.dfs(graph, in_degree)
        return res

    def build_graph(self, graph, in_degree, words):
        for word in words:
            for c in word:
                key = ord(c) - ord('a')
                graph[key] = set()

        for i in range(1, len(words)):
            first = words[i - 1]
            second = words[i]
            length = min(len(first), len(second))
            for c in range(length):
                if first[c] != second[c]:
                    _in = ord(second[c]) - ord('a')
                    _out = ord(first[c]) - ord('a')
                    if _in not in graph[_out]:
                        graph[_out].add(_in)
                        in_degree[_in] += 1
                    break

    def dfs(self, graph, in_degree):
        print(graph)
        print(in_degree)
        res = ''
        queue = [i for i in graph if in_degree[i] == 0]
        for q in queue:
            res += chr(q + ord('a'))
            for i in graph[q]:
                in_degree[i] -= 1
                if in_degree[i] == 0:
                    queue.append(i)

        if len(res) == len(graph):
            return res
        else:
            return ''