#!/usr/bin/env python3
# coding: utf-8

# Time complexity: O()
# Space complexity: O()

# https://leetcode.com/problems/evaluate-division/

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = collections.defaultdict(list)
        for edges, value in zip(equations, values):
            s, e = edges
            graph[s].append((e, value))
            graph[e].append((s, 1 / value))

        def calculate(query):
            s, e = query
            if s not in graph or e not in graph:
                return -1
            queue = collections.deque([(s, 1)])
            seen = set()
            while queue:
                node, cur_product = queue.popleft()
                if node == e:
                    return cur_product
                seen.add(node)
                for next_node, value in graph[node]:
                    if next_node not in seen:
                        queue.append((next_node, value * cur_product))

            return -1

        return [calculate(query) for query in queries]


